#stats(rows, key) -> dict (mean, median, std, count_nonnull)
#percentiles(values, p) -> float (quantile implementation)
#find_outliers(values) -> dict (IQR and z-score options)
#improvement(before_rows, after_rows) -> dict
import json
import transform

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

from typing import List, Dict, Callable, Iterable, Tuple, Any

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
