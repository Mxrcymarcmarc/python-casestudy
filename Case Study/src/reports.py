# printing and exporting of reports of the students
def print_report(student):
    print(f"Report for {student['name']}:")
    for subject, score in student['scores'].items():
        print(f"  {subject}: {score}")
