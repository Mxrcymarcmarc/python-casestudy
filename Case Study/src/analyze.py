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
import numpy as np
import math
import statistics
from matplotlib.ticker import MaxNLocator

def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)
    
def weighted_mean(quiz_avg, final, midterm, attendance, config):
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

"""
READ ME PLEASEEEEEEEE

to create a normal distribution graph, use extract scores first to compile all needed 
data into an array and assign it to a variable. Then call create_normal_dist() to make
the normal distribution that you need!
-------------------------------------------------------------------------------------
FUNCTION CALL EXAMPLE:
IT2_1_Midterms = extract_scores("BSIT 2-1", "Midterms")

create_normal_dist(IT2_1_Midterms, "Midterms", "red", True)
-------------------------------------------------------------------------------------
MULTIPLE NORMAL DISTRIBUTION EXAMPLE:
IT2_1_Midterms = extract_scores("BSIT 2-1", "Midterms")
IT2_2_Midterms = extract_scores("BSIT 2-2", "Midterms")

create_normal_dist([
    (IT2_1_Midterms, "Midterms", "blue", True),
    (IT2_1_Midterms, "Midterms", "red", True)
    ], title="Midterms Comparison")
    
"""

def extract_scores(section_data, category):
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

def create_normal_dist(datasets, title="Grade Distribution"): 
    # create_normal_dist([(Section_A, "Grades", "blue", True), title="title here"], 
    #                    [(Section_B, "Grades", "red", True), title="title here"])
    
    plt.figure(figsize=(10, 6))
    
    for data, category, color, fill in datasets:
        if isinstance(data[0], dict):
            values = extract_scores(data, category)
        else:
            values = data
        if values:
            normal_distribution(values, category, color, fill)
    
    plt.title(title, fontweight="bold")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    #plt.savefig(f"{title}.png", dpi=300)     # for saving graph as png.
    plt.show()                                # can be saved as PNG, PDF, SVG, or JPG.
    
def normal_distribution(values, category, color, fill=False):
    if not values:
        raise ValueError("Population cannot be empty")
    
    valid_categories = {"Grades", "Quiz", "Quizzes", "Midterms", "Finals"}
    if category not in valid_categories:
        raise ValueError(f"Invalid category. Must be one of: {valid_categories}")
    
    popu_len = len(values)
    mean = statistics.mean(values)
    stddev = stddev_compute(values, isPopulation=True)
    label = category
    
    x = random.normal(loc=mean, scale=stddev, size=popu_len)
    nd = sns.kdeplot(data=x, fill=fill, label=label, color=color)
    return nd

def stddev_compute(dataset, isPopulation=False):
    if not dataset:
        raise ValueError("Dataset cannot be empty")
        
    mean = statistics.mean(dataset)
    n = len(dataset)
    
    if not isPopulation: n -= 1
    return math.sqrt(sum((x - mean) ** 2 for x in dataset) / n)
           
def create_histogram(data, category, title="Histogram"): 
    plt.figure(figsize=(7, 4.3))
    
    # Get values (handles both student data and raw scores)
    values = extract_scores(data, category) if isinstance(data, list) else data

    plt.hist(values, bins='auto', alpha=0.9, color="#143371")

    # Make axes show whole numbers
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.title(title, fontweight="bold")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.grid(True, alpha=0.3)
    #plt.savefig(f"{title}.png", dpi=300)     # for saving graph as png.
    plt.show()                                # can be saved as PNG, PDF, SVG, or JPG.
    
def compute_percentile(values, percent):
    if not values: return None
    
    data = np.sort(values)
    val_len = len(values)
    
    k = (val_len - 1) * (percent/100)
    f = int(k)
    c = min(f + 1, val_len - 1)
    
    if f == c: return values[int(k)]
    else: return values[f] + (values[c] - values[f]) * (k - f)

def find_outliers(values):
    if not values:
        return {"outliers": [], "lower": None, "upper": None}
    
    q1 = compute_percentile(values, 25)
    q3 = compute_percentile(values, 75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [v for v in values if v < lower_bound or v > upper_bound]
    return {
        "outliers": outliers,
        "lower": round(lower_bound, 2),
        "upper": round(upper_bound, 2)
    }
    
def track_midterm_final_improvement(data):
    improvements = []
    details = []

    for student in data:
        midterm = student.get("midterm")
        final = student.get("final")

        if midterm is None or final is None:
            continue
        
        diff = final - midterm
        improvements.append(diff)
        details.append({
            "student_id": student["student_id"],
            "midterm": midterm,
            "final": final,
            "change": diff
        })
        
        if not improvements:
            return {"message": "No valid midterm/final data found."}
        
        avg_change = sum(improvements) / len(improvements)
        improved = sum(1 for d in improvements if d > 0)
        declined = sum(1 for d in improvements if d < 0)
        same = len(improvements) - improved - declined

        return {
            "average_change": round(avg_change, 2),
            "improved": improved,
            "declined": declined,
            "same": same,
            "details": details
        }

    