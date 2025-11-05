#compute_final(row, weights) -> float | None
#letter_grade(score, thresholds) -> str
#normalize_scores(rows), fill_missing_with_policy(rows, policy)
# computing the final grade, and letter grades
import json
import math

def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)
    
def quiz_average(quizzes):
    valid_scores = [q for q in quizzes if q is not None]
    
    if not valid_scores:
        return None
    else:
        return sum(q if q is not None else 0 for q in quizzes) / 5

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
    
def determine_lettergrade(grade, scale):
    if grade is None:
        return None
    
    for letter, bounds in scale.items():
        if bounds["min"] <= grade <= bounds["max"]:
            return letter
    return None
    
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
    

        
