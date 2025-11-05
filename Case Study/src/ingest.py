# this is where the csv file gets ingested and validated
import csv

def read_csv(file_path):
    students = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            student = {}
            
            student["student_id"] = row["student_id"].strip()
