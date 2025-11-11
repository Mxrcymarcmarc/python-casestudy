# reports.py
import csv
import os
from typing import Dict, List, Any
from utils import choose_section, format_student_one_line

Student = Dict[str, Any]
Records = Dict[str, List[Student]]

DEFAULT_OUTPUT_FOLDER = "reports"

def ensure_outdir(folder: str) -> None:
    os.makedirs(folder, exist_ok=True)

def export_section_csv(records: Records, output_folder: str = DEFAULT_OUTPUT_FOLDER) -> None:
    """
    Interactive export menu for section-level CSV exports.
    """
    while True:
        from menu import box_title
        box_title("EXPORT REPORTS")
        print("[1] Export a specific section")
        print("[2] Export ALL sections")
        print("[3] Back")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            section_name = choose_section(records)
            if not section_name:
                continue
            ensure_outdir(output_folder)
            filename = os.path.join(output_folder, f"{section_name.replace(' ', '_')}_report.csv")
            students = records.get(section_name, [])
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=[
                    "student_id","last_name","first_name","section",
                    "quizzes","quiz_average","midterm","final","attendance",
                    "final_grade","letter_grade","status"
                ])
                writer.writeheader()
                writer.writerows(students)
            print(f"Exported Section {section_name} as {filename}")
            input("Press Enter...")

        elif choice == "2":
            ensure_outdir(output_folder)
            for section_name, students in records.items():
                filename = os.path.join(output_folder, f"{section_name.replace(' ', '_')}_report.csv")
                with open(filename, mode="w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=[
                        "student_id","last_name","first_name","section",
                        "quizzes","quiz_average","midterm","final","attendance",
                        "final_grade","letter_grade","status"
                    ])
                    writer.writeheader()
                    writer.writerows(students)
                print(f"Exported: {filename}")
            print("All sections exported successfully.")
            input("Press Enter...")
            
        elif choice == "3":
            print("Returning to reports menu.")
            input("Press Enter...")
            return
        else:
            print("Invalid choice. Try again.")
            input("Press Enter...")

def export_atrisk_csv(records: Records, output_folder: str = DEFAULT_OUTPUT_FOLDER) -> None:
    ensure_outdir(output_folder)
    filename = os.path.join(output_folder, "AT_RISK_STUDENTS.csv")
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "last_name", "first_name", "section", "final_grade"])
        for section_name, students in records.items():
            for s in students:
                if s.get("status") == "At-Risk":
                    writer.writerow([
                        s.get("student_id"),
                        s.get("last_name"),
                        s.get("first_name"),
                        section_name,
                        s.get("final_grade")
                    ])
    print(f"At-risk list exported as {filename}")
    input("Press Enter...")

def print_summary(records: Records) -> None:
    """Prints a concise one-line-per-student summary across all sections."""
    from utils import format_student_one_line, clearscr
    clearscr()
    if not records:
        print("No records to show.")
        return
    print("=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    for section_name, students in records.items():
        print(f"\n=== Section: {section_name} ({len(students)} students) ===")
        for s in students:
            print(format_student_one_line(s))
    print("\n" + "=" * 60)
    input("Press Enter...")

def print_at_risk_students_summary(records: Records) -> None:
    from utils import format_student_one_line
    if not records:
        print("No records to show.")
        return
    print("=" * 60)
    print("AT-RISK STUDENTS SUMMARY")
    print("=" * 60)
    for section_name, students in records.items():
        at_risk_students = [s for s in students if s.get("status") == "At-Risk"]
        print(f"\n=== Section: {section_name} ({len(at_risk_students)} at-risk) ===")
        if not at_risk_students:
            print("No At-Risk Students in this section.")
            continue
        for s in at_risk_students:
            print(format_student_one_line(s))
    print("\n" + "=" * 60)
    input("Press Enter...")

def print_section_students_summary(records: Records) -> None:
    section_name = choose_section(records)
    if section_name is None:
        return
    students = records.get(section_name, [])
    print("=" * 60)
    print(f"SECTION SUMMARY: {section_name}")
    print("=" * 60)
    for s in students:
        print(format_student_one_line(s))
    print("\n" + "=" * 60)
    input("Press Enter...")

def print_section_at_risk_students_summary(records: Records) -> None:
    section_name = choose_section(records)
    if section_name is None:
        return
    students = [s for s in records.get(section_name, []) if s.get("status") == "At-Risk"]
    print("=" * 60)
    print(f"AT-RISK IN SECTION: {section_name}")
    print("=" * 60)
    if not students:
        print("No At-Risk Students in this section.")
    else:
        for s in students:
            print(format_student_one_line(s))
    print("\n" + "=" * 60)
    input("Press Enter...")