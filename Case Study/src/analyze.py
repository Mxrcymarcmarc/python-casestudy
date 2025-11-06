#stats(rows, key) -> dict (mean, median, std, count_nonnull)
#percentiles(values, p) -> float (quantile implementation)
#find_outliers(values) -> dict (IQR and z-score options)
#improvement(before_rows, after_rows) -> dict
import json
import transform
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
import statistics

def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)
    
def weighted_grade(quiz_avg, final, midterm, attendance, config):
    weights = config.get("weights", {})
    components = []
    weight_sum = 0.0

    if quiz_avg is not None and "quiz" in weights:
        components.append((quiz_avg, float(weights["quiz"])))
        weight_sum += float(weights["quiz"])
    if final is not None and "final" in weights:
        components.append((final, float(weights["final"])))
        weight_sum += float(weights["final"])
    if midterm is not None and "midterm" in weights:
        components.append((midterm, float(weights["midterm"])))
        weight_sum += float(weights["midterm"])
    if attendance is not None and "attendance" in weights:
        components.append((attendance, float(weights["attendance"])))
        weight_sum += float(weights["attendance"])

    if not components or weight_sum == 0:
        return None

    total = sum(value * w for value, w in components)
    return total / weight_sum

# NORMAL DISTRIBUTION 
# can be categorized by: Grades, Quizzes, Quiz, Midterms, Finals
def normal_distribution(population, category, color, fill=False):
    if not population:
        raise ValueError("Population cannot be empty")
    
    valid_categories = {"Grades", "Quiz", "Quizzes", "Midterms", "Finals"}
    if category not in valid_categories:
        raise ValueError(f"Invalid category. Must be one of: {valid_categories}")
    
    popu_len = len(population)
    mean = statistics.mean(population)
    stddev = stddev_compute(population, isPopulation=True)
    label = category
    
    x = random.normal(loc=mean, scale=stddev, size=popu_len)
    nd = sns.kdeplot(data=x, fill=fill, label=label, color=color)
    return nd

def create_normal_dist(datasets, title="Grade Distribution"): 
    # create_normal_dist([(Section_A, "Grades", "blue", True), title="title here"], 
    #                    [(Section_B, "Grades", "red", True), title="title here"])
    
    plt.figure(figsize=(10, 6))
    
    for population, category, color, fill in datasets:
        normal_distribution(population, category, color, fill)
    
    plt.title(title, fontweight="bold")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.show()

def stddev_compute(dataset, isPopulation=False):
    if not dataset:
        raise ValueError("Dataset cannot be empty")
        
    mean = statistics.mean(dataset)
    n = len(dataset)
    
    if not isPopulation: n -= 1
    return math.sqrt(sum((x - mean) ** 2 for x in dataset) / n)
           

def extract_scores(section_data, category):
    """
    Extracts a list of numeric scores for a given category.
    Handles quizzes individually, as a sum, or as a mean.
    """

    values = []

    for student in section_data:
        if category.lower().startswith("quiz") and len(category) > 4 and category[4:].isdigit():
            index = int(category[4:]) - 1  # quiz1 → index 0
            if 0 <= index < len(student["quizzes"]):
                q = student["quizzes"][index]
                if q is not None:
                    values.append(q)

        elif category.lower() in {"quiz_sum", "quizzes_sum"}:
            valid_quizzes = [q for q in student["quizzes"] if q is not None]
            if valid_quizzes:
                values.append(sum(valid_quizzes))

        elif category.lower() in {"quiz_mean", "quizzes_mean"}:
            valid_quizzes = [q for q in student["quizzes"] if q is not None]
            if valid_quizzes:
                values.append(sum(valid_quizzes) / len(valid_quizzes))

        elif category.lower() == "midterms":
            if student.get("midterm") is not None:
                values.append(student["midterm"])

        elif category.lower() == "finals":
            if student.get("final") is not None:
                values.append(student["final"])

        elif category.lower() == "grades":
            if "final_grade" in student and student["final_grade"] is not None:
                values.append(student["final_grade"])

    return values
