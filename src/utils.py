# utils.py
import os
from typing import Dict, List, Any, Optional

Student = Dict[str, Any]
Records = Dict[str, List[Student]]

# Clear Screen
def clearscr() -> None:
    """Clear terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")

# Choose Section from Records
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

# Format Student One-Line Summary
def format_student_one_line(student: Student) -> str:
    """
    Produce a compact single-line representation for student.
    Format: ID | Last, First | Final: 92.0 | Status: Pass
    """
    sid = student.get("student_id", "")
    last = student.get("last_name", "")
    first = student.get("first_name", "")
    final = student.get("final_grade")
    final_str = f"{final:.2f}" if isinstance(final, (int, float)) else "N/A"
    status = student.get("status", "N/A")
    return f"{sid} | {last}, {first} | Final: {final_str} | Status: {status}"

# Format the printing of Student Records
def pretty_print_students(section, title="Results"):
    print("\n" + "="*50)
    print(f"{title.center(50)}")
    print("="*50)

    if not section:
        print("No records found.\n")
        return

    for student in section:
        print("-" * 50)
        print(f"ID:        {student.get('student_id', '')}")
        print(f"Name:      {student.get('last_name', '')}, {student.get('first_name', '')}")
        
        quizzes = student.get("quizzes", [])
        q_scores = ", ".join(str(q) if q is not None else "-" for q in quizzes)
        print(f"Quizzes:   {q_scores}")

        print(f"Midterm:   {student.get('midterm', '-')}")
        print(f"Final:     {student.get('final', '-')}")
        print(f"Attend:    {student.get('attendance', '-')}")
        print(f"Q Avg:     {round(student.get('quiz_average', 0), 2) if student.get('quiz_average') is not None else '-'}")
        print(f"Final G:   {round(student.get('final_grade', 0), 2) if student.get('final_grade') is not None else '-'}")
        print(f"Letter:    {student.get('letter_grade', '-')}")
        print(f"Status:    {student.get('status', '-')}")
    print("="*50 + "\n")