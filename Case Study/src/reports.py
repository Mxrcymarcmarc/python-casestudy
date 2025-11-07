#print_summary(stats)
#export_section_csv(rows, out_dir)
#generate_at_risk_list(rows, threshold) -> List[dict]
# printing and exporting of reports of the students
# with open gawing function
# File Output for CSV Reports
import csv
import os
from typing import Dict, List, Any
from main import choose_section

Student = Dict[str, Any]
Records = Dict[str, List[Student]]

def clearscr():
    os.system("cls" if os.name == "nt" else "clear")

def export_section_csv(records: Records, output_folder="reports"):
    while True:
        clearscr()
        print("=== Export Reports Menu ===")
        print("1) Export a specific section")
        print("2) Export ALL sections")
        print("3) Back to Reports Menu")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            clearscr()
            print("\nAvailable Sections:")
            for idx, section in enumerate(records.keys(), start=1):
                print(f"{idx}. {section}")
            
            section_choice = input("\n Enter the section number (or B/b to go back): ")
            
            if section_choice.lower() == "b":
                continue
            
            try:
                section_name = list(records.keys())[int(section_choice) - 1]
            except:
                print("Invalid choice. Trying again.")
                continue
            
            os.makedirs(output_folder, exist_ok=True)
            filename = os.path.join(output_folder, f"{section_name.replace(' ', '_')}_report.csv")
            students = records[section_name]
            
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames= [
                    "student_id","last_name","first_name","section",
                    "quiz_average","midterm","final","attendance",
                    "final_grade","letter_grade","status"
                ])
                writer.writeheader()
                writer.writerows(students)
                
            print(f"Exported Section {section_name} as {filename}")
            
        elif choice == "2":
            os.makedirs(output_folder, exist_ok=True)
            
            for section, students in records.items():
                filename = os.path.join(output_folder, f"{section.replace(' ', '_')}_report.csv")
                
                with open(filename, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=[
                        "student_id","last_name","first_name","section",
                        "quiz_average","midterm","final","attendance",
                        "final_grade","letter_grade","status"
                    ])
                    writer.writeheader()
                    writer.writerows(students)
                    
                print(f"Exported: {filename}")
            print("All sections exported successfully.")
            
        elif choice == "3":
            print("Returning to reports menu.")
            return
        
        else:
            print("Invalid choice. Try again. ")
            continue
            
def export_atrisk_csv(records: Records, output_folder="reports"):
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, "AT_RISK_STUDENTS.csv")
    
    with open(filename, mode="w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "last_name", "first_name", "section", "final_grade"])
        
        for section, students in records.items():
            for s in students:
                if s.get("status") == "At-Risk":
                    writer.writerow([
                        s["student_id"],
                        s["last_name"],
                        s["first_name"],
                        section,
                        s["final_grade"]
                    ])
    print(f"At-risk list exported as {filename}")

def print_summary(records: Student):
    clearscr()
    print("="*40)
    print(f"{' '*13}Summary Report")
    print("="*40 + "\n")
    
    for section_name, section in records.items():
        print(f"\n{' '*4}=== Section: {section_name} ===")
        print(f"\nTotal Students: {len(section)}")

        # Student Details per section
        print("Student Details:\n")

        for student in section:
            print(f"#{student['student_id']}: {student['first_name']} {student['last_name']}")
            print(f"Final Grade: {student['final_grade']} | Letter Grade: {student['letter_grade']}")
            print(f"Status: {student['status']}\n")
        print("="*40)
        
def print_at_risk_students_summary(records: Student):
    clearscr()
    print("="*40)
    print(f"{' '*4}At Risk Students Summary Report")
    print("="*40 + "\n")
    
    for section_name, section in records.items():
        print(f"\n{' '*4}=== Section: {section_name} ===")
        print(f"\nTotal Students: {len(section)}")
        at_risk = 0
        
        # At-Risk Student Details per section
        print("Student Details:\n")
        
        for student in section:
            if student['status'] == 'At-Risk':
                print(f"#{student['student_id']}: {student['first_name']} {student['last_name']}")
                print(f"Final Grade: {student['final_grade']} | Letter Grade: {student['letter_grade']}")
                print(f"Status: {student['status']}\n")
                at_risk += 1
                
        if at_risk == 0:
            print("No At-Risk Students in this section.")
        else:
            print(f"Total At-Risk Students: {at_risk}")
        print("\n" + "="*40)

def print_section_students_summary(records: Student):
    clearscr()
    
    section = choose_section(records)
    if section is None:
        input("Press Enter...")
        return
    
    clearscr()
    print("="*40)
    print(f"{' '*8}Section Students Summary")
    print("="*40 + "\n")
    
    print(f"\n{' '*4}=== Section: {section} ===")
    print(f"\nTotal Students: {len(section)}")
    
    # Students Details per section
    print("Student Details:\n")
    for student in section:
        print(f"#{student['student_id']}: {student['first_name']} {student['last_name']}")
        print(f"Final Grade: {student['final_grade']} | Letter Grade: {student['letter_grade']}")
        print(f"Status: {student['status']}\n")
    print("="*40)

def print_section_at_risk_students_summary(records: Dict[str, Any]):
    clearscr()
    
    section = choose_section(records)
    if section is None:
        input("Press Enter...")
        return
    
    clearscr()
    print("="*40)
    print(f"Section At Risk Students Summary Report")
    print("="*40 + "\n")
    
    print(f"\n{' '*4}=== Section: {section} ===")
    print(f"\nTotal Students: {len(section)}")
    at_risk = 0
    
    # At-Risk Student Details per section
    print("Student Details:\n")
    for student in section:
        if student['status'] == 'At-Risk':
            print(f"#{student['student_id']}: {student['first_name']} {student['last_name']}")
            print(f"Final Grade: {student['final_grade']} | Letter Grade: {student['letter_grade']}")
            print(f"Status: {student['status']}\n")
            at_risk += 1
                
    if at_risk == 0:
        print("No At-Risk Students in this section.")
    else:
        print(f"Total At-Risk Students: {at_risk}")
    print("\n" + "="*40)