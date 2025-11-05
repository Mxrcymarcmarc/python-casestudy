# computing the final grade, and letter grades
import json
import statistics

def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)
    
def quiz_average(quizzes):
    valid_scores = [q for q in quizzes if q is not None]
    
    if not valid_scores:
        return None
    
    return statistics.mean(valid_scores)

def apply_weights(student, weights):
    quiz_average = student["quiz_average"]
    midterm = student["midterm"]
    final = student["final"]
    
def determine_lettergrade(grade, scale):
    if grade is None:
        return None
    
    for letter, bounds in scale.items():
        if bounds["min"] <= grade <= bounds["max"]:
            return letter
    return None
    
def transform(students, config):
    weights = config["weights"]
    scale = config["grade_scale"]
    thresholds = config["thresholds"]
    
    for student in students:
        student["quiz_average"] = quiz_average(student["quizzes"])
        student["final_grade"] = apply_weights(student, weights)
        
    

        