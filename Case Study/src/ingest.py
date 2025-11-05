# read_csv(path) -> List[dict]
#validate_row(row) -> Tuple[bool, list_of_errors]
#Handles trimming, parsing numbers, missing-to-None, score-range checks.
# this is where the csv file gets ingested and validated
import csv

def validate_row(row):
    errors = []
    
    required_fields = ["student_id", "last_name", "first_name", "section"]
    
    for field in required_fields:
        value = row.get(field, "").strip()
        if value == "":
            errors.append(f"Missing required field: {field}")
    
    return (len(errors) == 0, errors)

def read_csv(file_path):
    students = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            student = {}
    
            student["student_id"] = row["student_id"].strip()
            student["last_name"] = row["last_name"].strip()
            student["first_name"] = row["first_name"].strip()
            student["section"] = row["section"].strip()
            
            quizzes = []
            for i in range(1,6):
                q_number = row.get(f"quiz{i}", "").strip()
                quizzes.append(parse_score(q_number))
                
            student["quizzes"] = quizzes
            
            student["midterm"] = parse_score(row.get("midterm", "").strip())
            student["final"] = parse_score(row.get("final", "").strip())
            student["attendance"] = parse_score(row.get("attendance_percent", "").strip())
            
            students.append(student)
            
    return students

def parse_score(value):
    if value == "" or value is None:
        return None
    
    try:
        score = float(value)
        if 0 <= score <= 100:
            return score
    except ValueError:
        pass
    return None    


