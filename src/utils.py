# utils.py
import os
from typing import Dict, List, Any, Optional

Student = Dict[str, Any]
Records = Dict[str, List[Student]]

def clearscr() -> None:
    """Clear terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")

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