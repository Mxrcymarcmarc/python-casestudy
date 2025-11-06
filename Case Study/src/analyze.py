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

# NORMAL DISTRIBUTION 
# can be categorized by: Grades, Quizzes, Quiz, Midterms, Finals
def normal_distribution(population, category, label, color, fill=False):
    popu_len = len(population)
    mean = statistics.mean(population)
    stddev = stddev_compute(population, isPopulation=True)
    
    categories = pd.DataFrame({
        "Grades": random.normal(loc=mean, scale=stddev, size=popu_len),
        "Quiz": random.normal(loc=mean, scale=stddev, size=popu_len),
        "Quizzes": random.normal(loc=mean, scale=stddev, size=popu_len),
        "Midterms": random.normal(loc=mean, scale=stddev, size=popu_len),
        "Finals": random.normal(loc=mean, scale=stddev, size=popu_len)
    })
    
    nd = sns.kdeplot(data=categories[category], fill=False, label=label, color=color)
    return nd

def create_normal_dist(count):
    pass #djhekfbfhb WADAFAKKK T^T
    # plt.title("Comparison of Subject Distributions")
    # plt.legend(loc='upper right')
    # plt.show()

def stddev_compute(dataset, isPopulation=False):
    if not dataset:
        raise ValueError("Dataset cannot be empty")
        
    mean = statistics.mean(dataset)
    n = len(dataset)
    
    if not isPopulation: n -= 1
    return math.sqrt(sum((x - mean) ** 2 for x in dataset) / n)
    
#aaaaaaaaaaaaaaaa