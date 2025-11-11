# main pipeline
#orchestrates pipeline: load config, ingest, transform, analyze, reports, timing.
import os
import json
from ingest import read_csv
from transform import transform, load_config, select_rows, project_fields, sort_by, delete_student, insert_student
from reports import export_atrisk_csv, export_section_csv, clearscr
from analyze import (
    extract_scores, 
    create_normal_dist, 
    create_histogram,
    compute_percentile, 
    find_outliers,
    track_midterm_final_improvement, 
)

def ingest_file():
    clearscr()
    print("=== Ingest CSV File ===\n")
    path = input("Enter CSV file path: ").strip()

    if not os.path.exists(path):
        print("Error: File not found")
        input("\nPress Enter to return to menu...")
        return None
    
    print("\nLoading data...")
    
    records = read_csv(path)
    config = load_config()
    records = transform(records, config)
    
    print("File successfully ingested and processed.")
    input("\nPress Enter to return to main menu...")
    return records

def array_operations_menu(records):
    clearscr()
    print("=== Array Operations Menu ===\n")
    print("1) Select students")
    print("2) Project student fields")
    print("3) Sort students")
    print("4) Delete student")
    print("5) Insert student")
    print("6) Back")
    
    choice = input("\n Choose an option: ")
    
    if choice == "1":
        select_students(records)
    elif choice == "2":
        project_menu(records)
    elif choice == "3":
        sort_menu(records)
    elif choice == "4":
        delete_student_menu(records)
    elif choice == "5":
        insert_student_menu(records)
    elif choice == "6":
        return
    else:
        input("Invalid option. Press Enter...")

def choose_section(records):
    sections = list(records.keys())
    print("\nAvailable Sections:")
    for idx, sec in enumerate(sections, start=1):
        print(f"{idx}) {sec}")
        
    sec_choice = input("\nSelect section: ")
    
    if not sec_choice.isdigit() or not (1 <= int(sec_choice) <= len(sections)):
        print("Invalid Section.")
        return None
    return sections[int(sec_choice)-1]

def select_students(records):
    clearscr()
    print("=== Select Students ===")
    print("1) Passed")
    print("2) At-Risk")
    print("3) Incomplete")
    print("4) Failed")
    print("5) Back")
    
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
    print(f"=== Students ({status_map[choice]} in {section})")
    for s in result:
        print(s)
    input("\nPress Enter...")

def project_menu(records):
    clearscr()
    print("=== Project Fields ===")
    print("Choose fields to display: (comma separated)")
    print("Example: student_id,first_name,last_name,final_grade")
    
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
    
def sort_menu(records):
    clearscr()
    print("=== Sort Students===")
    print("1) Student ID")
    print("2) Last Name") 
    print("3) Midterm Grade")
    print("4) Final Grade")
    print("5) Back")
    
    choice = input("Choose how to sort: ")
    
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
    print("\nSort Order: ")
    print("1) Ascending ( A-Z / 0-100 )")
    print("2) Descending ( Z-A / 100-0 )")
    
    order = input("Choose Order: ")
    
    if order not in ["1", "2"]:
        print("Invalid sort order. Defaulting to Ascending.")
        reverse = False
    else:
        reverse = True if order == "2" else False
    
    sorted_list = sort_by(records[section], key_map[choice], reverse=reverse)
    
    clearscr()
    print(f"=== Sorted Students in {section} ===\n")
    for s in sorted_list:
        print(s)
    input("\nPress Enter...")
    
def delete_student_menu(records):
    clearscr()
    print("=== Delete Student ===")
    
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
    
def insert_student_menu(records):
    clearscr()
    print("=== Insert New Student ===")
    
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
        config = load_config()
        transform(records, config)
        print("\n Student successfuly added.")
    else:
        print("\nStudent ID already exists. Try again.\n")

def analytics_menu(records):
    while True:
        clearscr()
        print("=== Analytics Menu ===\n")
        print("1) Normal Distribution (Single Section)")
        print("2) Normal Distribution (Compare Sections)")
        print("3) Histogram")
        print("4) Compute Percentile")
        print("5) Find Outliers")
        print("6 Track Midterm to Final Improvements")
        print("7) Back")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            single_dist
    
def reports_menu(records):
    while True:
        clearscr()
        print("=== Reports Menu ===\n")
        print("1) Export Per-Section CSV")
        print("2) Export All At-Risk Students")
        print("3) Back")
    
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            export_section_csv(records)
            input("\n Press Enter to return...")
        elif choice == "2":
            export_atrisk_csv(records)
            input("\nPress Enter to return...")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
            input("Press Enter...")

def config_menu():
    config = load_config()
    
    while True:
        clearscr()
        print("=== Coniguration Menu ===\n")
        print("1) View current configuration")
        print("2) Edit weights")
        print("3) Edit grade scale")
        print("4) Edit thresholds")
        print("5) Reload config from file")
        print("6) Save changes")
        print("7) Load default configuration")
        print("8) Back")
        
        choice = input("Select an option: ")
        
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
            clearscr()
            print("=== Edit Grade Scale ===")
            print("Format: min max per letter (leave blank to skip)")
            for letter, bounds in config["grade_scale"].items():
                print(f"\n{letter}: ")
                new_min = input(f"  min ({bounds['min']}): ").strip()
                new_max = input(f"  max ({bounds['max']}): ").strip()
                if new_min:
                    config["grade_scale"][letter]["min"] = float(new_min)
                if new_max:
                    config["grade_scale"][letter]["max"] = float(new_max)
            print("\nGrade scale updated.")
            input("Press Enter...")
        
        elif choice == "4":
            clearscr()
            print("=== Edit Thresholds ===")
            for key, value in config["thresholds"].items():
                new = input(f"{key} ({value}): ").strip()
                if new:
                    config["thresholds"][key] = float(new)
            print("\nThresholds updated.")
            input("Press Enter...")
            
        elif choice == "5":
            config = load_config()
            print("\nConfiguration reloaded from file.")
            input("Press Enter...")
            
        elif choice == "6":
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
            print("\nConfiguration saved.")
            input("Press Enter...")
        
        elif choice == "7":
            clearscr()
            print("Restoring default configuration...")
            
            try:
                with open("config_default.json", "r") as f:
                    default_config = json.load(f)
                    
                with open("config.json", "w") as f:
                    json.dump(default_config, f, indent=4)
                
                config = load_config()
                print("\nDefaults restored successfully.")
            except FileNotFoundError:
                print("\n Error: config_default.json not found!")
            except Exception as e:
                print(f"\nAn error occurred: {e}")
            
            input("Press Enter...")
        
        elif choice == "8":
            return        

def main():
    records = None
    
    while True:
        clearscr()
        print("=== Academic Analytics Lite ===")
        print("=== Main Menu ===\n")
        print("1) Ingest CSV")
        print("2) Array Operations")
        print("3) Analytics")
        print("4) Reports")
        print("5) Configuration")
        print("6) Exit\n")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            records = ingest_file()
        
        elif choice in ["2", "3", "4"]:
            if records is None:
                print("\nPlease ingest a CSV file first.")
                input("Press Enter to continue...")
            else:
                if choice == "2":
                    array_operations_menu(records)
                elif choice == "3":
                    analytics_menu(records)
                elif choice == "4":
                    reports_menu(records)
        
        elif choice == "5":
            config_menu()
        
        elif choice == "6":
            clearscr()
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")
            
if __name__ == "__main__":
    main()

