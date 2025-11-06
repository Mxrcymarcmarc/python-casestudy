# printing and exporting of reports of the students
<<<<<<< HEAD

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
        
=======
def print_report(student):
    print(f"Report for {student['name']}:")
    for subject, score in student['scores'].items():
        print(f"  {subject}: {score}")
>>>>>>> 4fee51ff8f6663c3d731ac8fec24339676b5e2c3
