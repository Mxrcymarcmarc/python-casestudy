#stats(rows, key) -> dict (mean, median, std, count_nonnull)
#percentiles(values, p) -> float (quantile implementation)
#find_outliers(values) -> dict (IQR and z-score options)
#improvement(before_rows, after_rows) -> dict

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