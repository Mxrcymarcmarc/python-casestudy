
def box_title(title: str) -> None:
    line = "═" * (len(title) + 8)
    print(f"╔{line}╗")
    print(f"║    {title}    ║")
    print(f"╚{line}╝")


def main_menu():
    box_title("ACADEMIC ANALYTICS LITE")
    box_title("MAIN MENU")
    print("[1] Ingest CSV")
    print("[2] Array Operations")
    print("[3] Analytics")
    print("[4] Reports")
    print("[5] Configuration")
    print("[6] Exit")


def array_operations_menu():
    box_title("ARRAY OPERATIONS")
    print("[1] Select Students")
    print("[2] Project Fields")
    print("[3] Sort Students")
    print("[4] Insert Student")
    print("[5] Delete Student")
    print("[6] Back")


def select_menu():
    box_title("SELECT STUDENTS")
    print("[1] Passed")
    print("[2] At-Risk")
    print("[3] Incomplete")
    print("[4] Failed")
    print("[5] Back")


def sort_menu():
    box_title("SORT STUDENTS BY")
    print("[1] Student ID")
    print("[2] Last Name")
    print("[3] Midterm Grade")
    print("[4] Final Grade")
    print("[5] Back")


def sort_order_menu():
    box_title("SORT ORDER")
    print("[1] Ascending   (A-Z / 0-100)")
    print("[2] Descending  (Z-A / 100-0)")


def reports_menu():
    box_title("REPORTS")
    print("[1] Print Summary")
    print("[2] Export CSVs Menu")
    print("[3] Generate At-Risk List")
    print("[4] Back")

def export_submenu():
    box_title("EXPORT CSVs MENU")
    print("[1] Export PER Section")
    print("[2] Export ALL At-Risk List")
    print("[3] Back")

def select_sec(title):
    box_title(title)
    print("[1] Specific Section")
    print("[2] ALL Sections")
    print("[3] Back")

def config_menu():
    box_title("CONFIGURATION")
    print("[1] Load JSON Config")
    print("[2] Edit Config Values")
    print("[3] Restore Defaults")
    print("[4] Back")


def print_fields_menu():
    box_title("PROJECT FIELDS")
    print("Enter comma-separated fields.")
    print("Example: student_id,last_name,midterm,final_grade")
    
def analytics_menu():
    box_title("ANALYTICS MENU")
    print("[1] Normal Distribution (Single Section)")
    print("[2] Normal Distribution (Compare Sections)")
    print("[3] Histogram")
    print("[4] Compute Percentile")
    print("[5] Find Outliers")
    print("[6] Track Midterm -> Final Improvements")
    print("[7] Back")
    
def config_menu():
    box_title("CONFIGURATION MENU")
    print("[1] View current configuration")
    print("[2] Edit weights")
    print("[3] Edit grade scale")
    print("[4] Edit thresholds")
    print("[5] Reload config from file")
    print("[6] Save changes")
    print("[7] Load default configuration")
    print("[8] Back")