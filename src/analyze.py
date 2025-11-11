from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import statistics
from matplotlib.ticker import MaxNLocator
from typing import List, Dict, Any

Student = Dict[str, Any]
Section = List[Student]

# Calculate weighted mean based on provided weights in config
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

# Extract scores from student records based on category
def extract_scores(section: Section, category):
    values = []

    for student in section:
        if category.startswith("quiz") and category[4:].isdigit():
            quiz_index = int(category[4:]) - 1
            return [s["quizzes"][quiz_index] for s in section if isinstance(s.get("quizzes"), list)]
        
        elif category.lower() in {"quiz_sum", "quizzes_sum"}:
            valid_quizzes = [q for q in student["quizzes"] if q is not None]
            if valid_quizzes:
                values.append(sum(valid_quizzes))

        elif category.lower() in {"quiz_mean", "quizzes_mean"}:
            valid_quizzes = [q for q in student["quizzes"] if q is not None]
            if valid_quizzes:
                values.append(sum(valid_quizzes) / len(valid_quizzes))

        elif category.lower() in {"midterm", "midterms"}:
            if student.get("midterm") is not None:
                values.append(student["midterm"])

        elif category.lower() in {"final","finals"}:
            if student.get("final") is not None:
                values.append(student["final"])

        elif category.lower() == "grades":
            if "final_grade" in student and student["final_grade"] is not None:
                values.append(student["final_grade"])

    return values

# Create normal distribution plots
def create_normal_dist(*args, title="Grade Distribution"):

    plt.figure(figsize=(10, 6))

    if len(args) == 1 and isinstance(args[0], list):
        datasets = args[0]
    elif len(args) == 2 and isinstance(args[0], tuple) and isinstance(args[1], tuple):
        # Handle 2 tuple arguments
        datasets = [args[0], args[1]]
    else:
        # Pack args into groups of 4
        if len(args) % 4 != 0:
            raise ValueError("create_normal_dist requires sets of 4 args: values, category, color, fill")
                        
        datasets = []
        for i in range(0, len(args), 4):
            datasets.append((args[i], args[i+1], args[i+2], args[i+3]))

    for values, category, color, fill in datasets:
        # If student dicts, convert to scores
        if values and isinstance(values[0], dict):
            values = extract_scores(values, category)

        if values:
            normal_distribution(values, category, color, fill)

    plt.title(title, fontweight="bold")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.savefig(f"{title}.png", dpi=300)
    plt.show()

# Generate normal distribution for a given set of values
def normal_distribution(values, category, color, fill=False):
    if not values:
        raise ValueError("Population cannot be empty")

    valid_categories = {
    "quiz", "quizzes", "midterm", "midterms", "final", "finals",
    "grades", "grade", "quiz_sum", "quiz_mean", "final_grade"
    }

    if category.lower().startswith("quiz"):
        quiz_suffix = category.lower()[4:]
        if quiz_suffix.isdigit() and 1 <= int(quiz_suffix) <= 5:
            pass  # valid quizN
        elif category.lower() in valid_categories:
            pass  # valid named category
        else:
            raise ValueError(f"Invalid category: {category}. Must be a quiz1-5 or one of {valid_categories}")

    popu_len = len(values)
    mean = statistics.mean(values)
    stddev = stddev_compute(values, isPopulation=True)

    x = random.normal(loc=mean, scale=stddev, size=popu_len)
    sns.kdeplot(data=x, fill=fill, label=category, color=color)

# Compute standard deviation
def stddev_compute(dataset, isPopulation=False):
    if not dataset:
        raise ValueError("Dataset cannot be empty")
        
    mean = statistics.mean(dataset)
    n = len(dataset)
    
    if not isPopulation: n -= 1
    return math.sqrt(sum((x - mean) ** 2 for x in dataset) / n)

# Create histogram for given data and category    
def create_histogram(data, category, title="Histogram", color="#143371"):
    plt.figure(figsize=(7, 4.3))

    if isinstance(data, list):
        if data and isinstance(data[0], dict):
            values = extract_scores(data, category)
        else:
            values = data
    else:
        values = data

    plt.hist(values, bins='auto', alpha=0.9, color=color)

    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.title(title, fontweight="bold")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.grid(True, alpha=0.3)
    plt.savefig(f"{title}.png", dpi=300)
    plt.show()
    plt.show()

# Compute percentile value
def compute_percentile(values, percent):
    if not values: return None
    
    data = np.sort(values)
    val_len = len(values)
    
    k = (val_len - 1) * (percent/100)
    f = int(k)
    c = min(f + 1, val_len - 1)
    
    if f == c: return data[int(k)]
    else: return data[f] + (data[c] - data[f]) * (k - f)

# Identify outliers using IQR method
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

# Track midterm to final exam improvements
def track_midterm_final_improvement(section: Section):
    improvements = []
    details = []

    for student in section:
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
