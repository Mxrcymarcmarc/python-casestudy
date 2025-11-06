
# this is where the csv file gets ingested and validated
import csv
#scans each row if they have the required fields and sends out an error message if not
def validate_row(row):
    errors = []
    
    required_fields = ["student_id", "last_name", "first_name", "section"]
    
    for field in required_fields:
        value = row.get(field, "").strip()
        if value == "":
            errors.append(f"Missing required field: {field}")
    
    return (len(errors) == 0, errors)

#reads the csv file and iterates per row to create a list of student dicts
def read_csv(file_path):
    records = {}
    row_number = 1

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            row_number += 1
            is_valid, errors = validate_row(row)
            
            if not is_valid:
                print(f"[ERROR] Row {row_number} skipped:")
                for err in errors:
                    print(f"   -> {err}")
                continue
            
            
            student = {}
            
            student["student_id"] = row["student_id"].strip()
            student["last_name"] = row["last_name"].strip()
            student["first_name"] = row["first_name"].strip()
            section_name = row["section"].strip()
            student["section"] = section_name
            
            quizzes = []
            for i in range(1,6): 
                q_number = row.get(f"quiz{i}", "").strip()
                quizzes.append(parse_score(q_number))
                
            student["quizzes"] = quizzes
            
            student["midterm"] = parse_score(row.get("midterm", "").strip())
            student["final"] = parse_score(row.get("final", "").strip())
            student["attendance"] = parse_score(row.get("attendance_percent", "").strip())
            
            """
            Program Structure of Records
            {
                "BSIT 2-1" : [{ "student_id" : "0001", 
                                "last_name" : "celis", 
                                "first_name" : "marc",
                                "section" : "BSIT 2-1"
                                "quizzes" : [80, 90, None, 98, 21]
                                "midterm" : 80
                                "final" : 90
                                "attendance" : 100}]
                "BSIT 2-2" : [{student2}]
            }"""
            
            if section_name not in records:
                records[section_name] = []
            records[section_name].append(student)
            
    return records

#checks if the value entered in the csv file for the scores is valid or will be returned as None
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


