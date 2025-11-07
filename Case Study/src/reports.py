#print_summary(stats)
#export_section_csv(rows, out_dir)
#generate_at_risk_list(rows, threshold) -> List[dict]
# printing and exporting of reports of the students

# File Output for CSV Reports
import csv
import os
from typing import Dict, List, Any

Student = Dict[str, Any]
Records = Dict[str, List[Student]]

def clearscr():
    if os.name =="nt":
        os.system('cls')

def export_section_csv(records: Records, output_folder="reports"):
    while True:
        clearscr()
        print("Export Reports Menu")
        print("(1) Export a specific section")
        print("(2) Export ALL sections")
        print("(3) Back to Reports Menu")
        
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
            filename = os.path.join(output_folder, f"{section_name.replace(' ', '_')}")
            students = records[section_name]
            
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames= [
                    "student_id","last_name","first_name","section",
                    "quiz_average","midterm","final","attendance",
                    "final_grade","letter_grade","status"
                ])
                writer.writeheader()
                writer.writerows(students)
                
            print(f"Exported Section {section_name}: {filename}")
            
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
            
def print_summary(records: Dict[str, Any]):
    clearscr()
    print("="*15)
    print("Summary Report")
    print("="*15 + "\n")
    
    for section_name, section in records.items():
        print(f"\nSection: {section_name}")
        print(f"Total Students: {len(section)}")

        # Student Details per section
        print("\nStudent Details:")
        print("="*40 + "\n")
        for student in section:
            print(f"#{student['student_id']}: {student['first_name']} {student['last_name']}")
            print(f"Final Grade: {student['final_grade']} | Letter Grade: {student['letter_grade']}")
            print(f"Status: {student['status']}\n")
        print("="*40)
        
def print_at_risk_students_summary(records: Dict[str, Any]):
    clearscr()
    print("="*25)
    print("At Risk Students Summary Report")
    print("="*2)
    
    for section_name, section in records.items():
        print(f"\nSection: {section_name}")
        print(f"Total Students: {len(section)}")
        at_risk = 0
        
        # At-Risk Student Details per section
        print("\nStudent Details:")
        print("="*40 + "\n")
        
        for student in section:
            if student['status'] == 'At-Risk':
                print(f"#{student['student_id']}: {student['first_name']} {student['last_name']}")
                print(f"Final Grade: {student['final_grade']} | Letter Grade: {student['letter_grade']}")
                print(f"Status: {student['status']}\n")
                at_risk += 1
                
        if at_risk == 0:
            print("No At-Risk Students in this section.")
        else:
            print(f"Total At-Risk Students in {section_name}: {at_risk}")
        print("\n" + "="*40)
            