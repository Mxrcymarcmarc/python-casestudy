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

def weights(student, weights):
    quiz_average = student["quiz_average"]
    midterm = student["midterm"]
    final = student["final"]