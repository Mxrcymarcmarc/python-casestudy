#compute_final(row, weights) -> float | None
#letter_grade(score, thresholds) -> str
#normalize_scores(rows), fill_missing_with_policy(rows, policy)
# computing the final grade, and letter grades
import json
import math
from typing import List, Dict, Callable, Iterable, Any

Student = Dict[str, Any]
Section = List[Student]

# Array Operations
def select_rows(section: Section, predicate: Callable[[Student], bool]) -> Section:
    return [s for s in section if predicate(s)]

def project_fields(section: Section, fields: Iterable[str]) -> List[Dict[str, Any]]:
    return [[{k: s.get(k) for k in fields} for s in section]]

def sort_by(section: Section, key_fn: Callable[[Student], Any], reverse: bool = False) -> Section:
    return sorted(section, key=key_fn, reverse=reverse)

def delete_student(section: Section, student_id: str) -> bool:
    for i, s in enumerate(section):
        if s.get("student_id") == student_id:
            del section[i]
            return True

    return False

#loading config.json as a python object
def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)

#computing quiz averages
def quiz_average(quizzes):
    valid_scores = [q for q in quizzes if q is not None]
    
    if not valid_scores:
        return None
    else:
        return sum(q if q is not None else 0 for q in quizzes) / 5

#applying weights from config file to grades
def apply_weights(student, weights):
    quiz_average = student["quiz_average"]
    midterm = student["midterm"]
    final = student["final"]
    attendance = student["attendance"]
    
    grade_components = [quiz_average, midterm, final, attendance]
    if any(x is None for x in grade_components):
        return None
    
    weighted_grade = (
        quiz_average * weights["quiz"] +
        midterm * weights["midterm"] +
        final * weights["final"] +
        attendance * weights["attendance"]
    )
    
    return math.floor(weighted_grade * 100)/100

#determining the letter grade based on the final grade  
def determine_lettergrade(grade, scale):
    if grade is None:
        return None
    
    for letter, bounds in scale.items():
        if bounds["min"] <= grade <= bounds["max"]:
            return letter
    return None

#computes for the overall score of the student
def transform(section, config):
    weights = config["weights"]
    scale = config["grade_scale"]
    thresholds = config["thresholds"]
    
    for student in section:
        student["quiz_average"] = quiz_average(student["quizzes"])
        student["final_grade"] = apply_weights(student, weights)
        student["letter_grade"] = determine_lettergrade(student["final_grade"], scale)
        
        if student["final_grade"] is None:
            student["status"] = "Incomplete"
        elif student["final_grade"] < thresholds["at_risk"]:
            student["status"] = "At-Risk"
        elif student["final_grade"] >= thresholds["pass"]:
            student["status"] = "Pass"
        else:
            student["status"] = "Fail"
            
    return section    
    

        
