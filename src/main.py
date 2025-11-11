# main pipeline
#orchestrates pipeline: load config, ingest, transform, analyze, reports, timing.
import os
import json
from ingest import read_csv
from transform import transform, load_config, select_rows, project_fields, sort_by, delete_student, insert_student
from analyze import extract_scores, create_normal_dist, create_histogram,compute_percentile, find_outliers, track_midterm_final_improvement
from reports import export_atrisk_csv, export_section_csv, print_summary, print_at_risk_students_summary, print_section_students_summary, print_section_at_risk_students_summary
from menu import box_title, main_menu, array_operations_menu, select_menu, sort_menu, sort_order_menu, reports_menu, config_menu, print_fields_menu, analytics_menu, select_sec, export_submenu, print_categories_histogram, print_categories
from utils import choose_section, clearscr, pretty_print_students

# Ingest CSV file
def ingest_file():
    clearscr()
    box_title("INGEST CSV FILE")
    path = input("Enter CSV file path: ").strip()

    if not os.path.exists(path):
        print("Error: File not found")
        input("\nPress Enter to return to menu...")
        return None
    
    print("\nLoading data...")
    
    records = read_csv(path)
    config = load_config("config.json")
    records = transform(records, config)
    
    print("File successfully ingested and processed.")
    input("\nPress Enter to return to main menu...")
    return records

# Array Operations Main Menu
def array_operations_main(records):
    clearscr()
    array_operations_menu()
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":
        select_students(records)
    elif choice == "2":
        project_menu(records)
    elif choice == "3":
        sort_main(records)
    elif choice == "4":
        insert_student_menu(records)
    elif choice == "5":
        delete_student_menu(records)
    elif choice == "6":
        return
    else:
        input("Invalid option. Press Enter...")

# Select Students Submenu
def select_students(records):
    clearscr()
    select_menu()
    
    choice = input("\nChoose what to select: ")
    
    status_map = {
        "1" : "Pass",
        "2" : "At-Risk",
        "3" : "Incomplete",
        "4" : "Fail"
    }
    
    if choice not in status_map:
        return
    
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return

    result = select_rows(records[section], lambda s: s.get("status") == status_map[choice])
    
    clearscr()
    titles = {
        "1": "Passing Students",
        "2": "At-Risk Students",
        "3": "Incomplete Students",
        "4": "Failing Students"
    }
    
    pretty_print_students(result, titles[choice])
    input("\nPress Enter...")

# Project Fields Submenu
def project_menu(records):
    clearscr()
    print_fields_menu()
    
    fields = input("Fields: ").replace(" ", "").split(",")
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    projected = project_fields(records[section], fields)
    
    clearscr()
    print(f"=== Projected Fields in {section} ===\n")
    for row in projected:
        print(row)
    input("\nPress Enter...")

# Sort Students Submenu
def sort_main(records):
    clearscr()
    sort_menu()
    
    choice = input("\nChoose how to sort: ")
    
    key_map = {
        "1" : lambda s: s.get("student_id"),
        "2" : lambda s: s.get("last_name"),
        "3" : lambda s: s.get("midterm", 0),
        "4" : lambda s: s.get("final_grade", 0)
    }
    
    if choice == "5":
        return
    
    if choice not in key_map:
        input("Invalid choice. Press Enter...")
        return
    
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    clearscr()
    sort_order_menu()
    
    order = input("\nChoose Order: ")
    
    if order not in ["1", "2"]:
        print("Invalid sort order. Defaulting to Ascending.")
        reverse = False
    else:
        reverse = True if order == "2" else False
    
    sorted_list = sort_by(records[section], key_map[choice], reverse=reverse)
    
    clearscr()
    # print(f"=== Sorted Students in {section} ===\n")
    # for s in sorted_list:
    #     print(s)
    
    titles = {
        "1": "Sorted by Student-ID",
        "2": "Sorted by Last Name",
        "3": "Sorted by Midterm Scores",
        "4": "Sorted by Final Grade"
    }

    pretty_print_students(sorted_list, titles[choice])
    
    input("\nPress Enter...")

# Delete Student Submenu   
def delete_student_menu(records):
    clearscr()
    box_title("DELETE STUDENT")
    
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    id = input("Enter Student ID to delete: ")
    
    success = delete_student(records[section], id)
    if success:
        print("Student deleted.")
    else:
        print("Student not found.")
    input("Press Enter...")

# Insert Student Submenu   
def insert_student_menu(records):
    clearscr()
    box_title("INSERT NEW STUDENT")
    
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    print("\nEnter new student details:")
    student_id = input("Student ID: ")
    first = input("First Name: ")
    last = input("Last Name: ")
    
    quizzes = []
    print("\nEnter 5 quiz scores (use -1 for missing quiz)")
    for i in range(1,6):
        q = input(f"Quiz {i}: ")
        quizzes.append(int(q) if q.isdigit() else None)
    
    midterm = float(input("Midterm: "))
    final = float(input("Final: "))
    attendance = float(input("Attendance: "))
    
    new_student = {
        "student_id" : student_id,
        "first_name" : first,
        "last_name" : last,
        "quizzes" : quizzes,
        "midterm" : midterm,
        "final" : final,
        "attendance" : attendance
    }
    
    success = insert_student(records[section], new_student)
    if success:
        config = load_config("config.json")
        records = transform(records, config)
        print("\n Student successfuly added.")
        input("Press Enter...")
    else:
        input("\nStudent ID already exists. Press Enter...\n")
        
# Analytics Main Menu
def analytics_main(records):
    while True:
        clearscr()
        analytics_menu()
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            single_normal_dist(records)
        elif choice == "2":
            multi_normal_dist(records)
        elif choice == "3":
            histogram_menu(records)
        elif choice == "4":
            percentile_menu(records)
        elif choice == "5":
            outliers_menu(records)
        elif choice == "6":
            improvement_menu(records)
        elif choice == "7":
            return
        else:
            input("Invalid option. Press Enter...")
            
# Single Normal Distribution Submenu     
def single_normal_dist(records):
    clearscr()
    box_title("SINGLE NORMAL DISTRIBUTION")
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
       
    category = print_categories()
    if not category:
        input("Press Enter...")
        return
        
    values = extract_scores(records[section], category)
    if not values:
        input("No available data. Press Enter...")
        return
    
    create_normal_dist(values, category, "blue", True, title=f"{section} {category} Normal Distribution")
    input("\nPress Enter...")

# Multi Normal Distribution Submenu    
def multi_normal_dist(records):
    clearscr()
    box_title("MULTI-NORMAL DISTRIBUTION")
    s1 = choose_section(records)
    s2 = choose_section(records)
    
    if not s1 or not s2:
        input("Press Enter...")
        return
    
    category = print_categories()
    if not category:
        input("Press Enter...")
        return
    
    d1 = extract_scores(records[s1], category)
    d2 = extract_scores(records[s2], category)
    
    create_normal_dist(
        (d1, category, "blue", True),
        (d2, category, "red", True), title=f"{category} Comparison: {s1} & {s2}")
    
    input("Press Enter...")
 
# Histogram Submenu   
def histogram_menu(records):
    clearscr()
    box_title("HISTOGRAM")
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    category = print_categories_histogram()
    if not category:
        input("Press Enter...")
        return
    
    data = extract_scores(records[section], category)
    
    create_histogram(data, category, title=f"{section} {category} Histogram")
    input("Press Enter...")    

# Percentile Submenu    
def percentile_menu(records):
    clearscr()
    box_title("COMPUTE PERCENTILE")
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    category = print_categories()
    if not category:
        input("Press Enter...")
        return
    
    percent = float(input("Percentile (0-100): "))
    
    value = extract_scores(records[section], category)
    result = compute_percentile(value, percent)
    
    if result:
        print(f"\nThe {percent}th percentile of {section} {category}: {result}")
        input("\nPress Enter...")
    else:
        print("No data available for that category.")

# Outliers Submenu   
def outliers_menu(records):
    clearscr()
    box_title("FIND OUTLIERS")
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    category = print_categories()
    if not category:
        input("Press Enter...")
        return
    
    value = extract_scores(records[section], category)
    result = find_outliers(value)
    
    print(f"\nOutliers in {section} for {category}: {result['outliers']}")
    print(f"Lower bound: {result['lower']}, Upper bound: {result['upper']}")
    input("\nPress Enter...")

# Midterm to Final Improvements Submenu    
def improvement_menu(records):
    clearscr()
    box_title("MIDTERM -> FINAL IMPROVEMENTS")
    section = choose_section(records)
    if not section:
        input("Press Enter...")
        return
    
    result = track_midterm_final_improvement(records[section])
    clearscr()

    box_title("IMPROVEMENT RESULTS")
    print(json.dumps(result, indent=4))
    input("\nPress Enter...")
    
# Reports Main Menu
def reports_main(records):
    while True:
        clearscr()
        reports_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            print_summary_main(records)
        elif choice == "2":
            export_menu(records)
        elif choice == "3":
            gen_at_risk(records)
        elif choice == "4": 
            return
        else:
            print("Invalid choice.")
            input("Invalid option. Press Enter...")

# Print Summary Submenu
def print_summary_main(records):
    clearscr()
    while True:
        select_sec("PRINT SUMMARY")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1": 
            print_section_students_summary(records)
        elif choice == "2":
            print_summary(records)
        elif choice == "3":
            return
        else:
            input("Invalid input. Press Enter...")  

# Export CSVs Submenu            
def export_menu(records):
    clearscr()
    while True:
        export_submenu()
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            export_section_csv(records)
        elif choice == "2":
            export_atrisk_csv(records)
        elif choice == "3":
            return
        else: 
            input("Invalid option. Press Enter...")

# Generate At-Risk List Submenu            
def gen_at_risk(records):
    clearscr()
    while True:
        select_sec("GENERATE AT-RISK LIST")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            print_section_at_risk_students_summary(records)
        elif choice == "2":
            print_at_risk_students_summary(records)
        elif choice == "3":
            return
        else:
            input("Invalid option. Press Enter...")
            
# Configuration Main Menu        
def config_main():
    config = load_config("config.json")
    
    while True:
        clearscr()
        config_menu()
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            clearscr()
            print("=== Current Configuration ===")
            print(json.dumps(config, indent=4))
            input("\nPress Enter...")
            
        elif choice == "2":
            clearscr()
            print("=== Edit Weights ===")
            for key, value in config["weights"].items():
                new = input(f"{key} ({value}): ").strip()
                if new:
                    config["weights"][key] = float(new)
            print("\nWeights updated.")
            input("Press Enter...")
            
        elif choice == "3":
            config = load_config("config.json")
            print("\nConfiguration reloaded from file.")
            input("Press Enter...")
            
        elif choice == "4":
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
            print("\nConfiguration saved.")
            input("Press Enter...")
        
        elif choice == "5":
            clearscr()
            print("Restoring default configuration...")
            
            try:
                with open("config_default.json", "r") as f:
                    default_config = json.load(f)
                    
                with open("config.json", "w") as f:
                    json.dump(default_config, f, indent=4)
                
                config = load_config("config_default.json")
                print("\nDefaults restored successfully.")
            except FileNotFoundError:
                print("\n Error: config_default.json not found!")
            except Exception as e:
                print(f"\nAn error occurred: {e}")
            
            input("Press Enter...")
        
        elif choice == "6":
            return        
        
        else: 
            input("Invalid option. Press Enter...")
            
# Main Function
def main():
    records = None
    
    while True:
        clearscr()
        main_menu()
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            records = ingest_file()
        
        elif choice in ["2", "3", "4"]:
            if records is None:
                print("\nPlease ingest a CSV file first.")
                input("Press Enter to continue...")
            else:
                if choice == "2":
                    array_operations_main(records)
                elif choice == "3":
                    analytics_main(records)
                elif choice == "4":
                    reports_main(records)
        
        elif choice == "5":
            config_main()
        
        elif choice == "6":
            clearscr()
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice.")
            input("Press Enter to retry...")
            
# Run main function            
if __name__ == "__main__":
    main()

