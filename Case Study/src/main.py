# main pipeline
#orchestrates pipeline: load config, ingest, transform, analyze, reports, timing.
# main.py

import json
import os
from typing import List, Dict, Any

# Import project modules
import time
import ingest
import transform
import analyze
import reports

# ===================================== #
# GLOBAL VARIABLES
# ===================================== #

data = []  # will hold loaded CSV data
config = {}  # will hold loaded config.json
data_loaded = False


# ===================================== #
# UTILITY FUNCTIONS
# ===================================== #

def check_required_files():
    """Ensure config.json and input.csv exist before program runs."""
    missing_files = []
    for file in ["config.json", "input.csv"]:
        if not os.path.exists(file):
            missing_files.append(file)
    if missing_files:
        print(f"⚠️ Missing required files: {', '.join(missing_files)}")
        print("Please make sure both config.json and input.csv are available in the folder.")
        return False
    print("Required files found and ready.")
    return True


def load_startup_files():
    """Load config.json and input.csv at the start."""
    global config, data, data_loaded
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        print("✅ Config loaded successfully.")
    except Exception as e:
        print(f"⚠️ Failed to load config.json: {e}")
        config = {}

    try:
        data = ingest.read_csv("input.csv")
        data_loaded = True
        print(f"✅ Input CSV loaded successfully — {len(data)} records found.")
    except Exception as e:
        print(f"⚠️ Failed to load input.csv: {e}")
        data_loaded = False


# ===================================== #
# MAIN MENU
# ===================================== #

def main_menu():
    """Display main menu and handle user input"""
    global data_loaded
    while True:
        print("\n====== Academic Analytics Lite ======")
        print("1) Clean ingest")
        print("2) Array operations: Select, project, sort, insert, and delete.")
        print("3) Analytics: Weighted grades, distributions, percentiles, outliers, improvements.")
        print("4) Reports: Print summary, export per-section CSVs, and generate 'at-risk' lists.")
        print("5) Configuration: Load/edit JSON config.")
        print("6) Exit")
        print("=====================================")

        choice = input("Enter your choice (1-6): ").strip()

        # Restrict access to options until data is loaded
        if not data_loaded and choice not in ["1", "5", "6"]:
            print("\n You must first complete 'Clean ingest' (Option 1) before using other modules.")
            continue

        if choice == "1":
            clean_ingest_menu()
        elif choice == "2":
            array_operations_menu()
        elif choice == "3":
            analytics_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            configuration_menu()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ===================================== #
# SUB-MENUS
# ===================================== #



# ===================================== #
# ingest.py
# ===================================== #

def clean_ingest_menu():
    """Menu for data ingestion"""
    global data_loaded, data
    while True:
        print("\n--- Clean Ingest Menu ---")
        print("1) Read CSV file (input.csv)")
        print("2) Validate and view sample records")
        print("3) Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                print("\n📂 Reading CSV file: input.csv ...")
                data = ingest.read_csv("input.csv")   # ✅ Correctly calls function from ingest.py
                data_loaded = True

                total_sections = len(data)
                total_students = sum(len(students) for students in data.values())
                print(f"✅ Successfully loaded {total_students} students across {total_sections} sections!")
            except FileNotFoundError:
                print("⚠️ 'input.csv' not found! Please make sure it exists in the project directory.")
            except Exception as e:
                print(f"⚠️ An unexpected error occurred while reading CSV: {e}")

        elif choice == "2":
            if not data_loaded:
                print("⚠️ No data loaded yet. Please run option 1 first.")
                continue

            # Ask how user wants to preview data
            print("\nPreview Options:")
            print("1) Show all students")
            print("2) Show a specific number of students per section")

            preview_choice = input("Enter choice (1 or 2): ").strip()

            if preview_choice == "1":
                preview_limit = None  # Show all
            elif preview_choice == "2":
                try:
                    preview_limit = int(input("Enter number of students to display per section: "))
                    if preview_limit <= 0:
                        print("⚠️ Number must be greater than 0. Defaulting to 3.")
                        preview_limit = 3
                except ValueError:
                    print("⚠️ Invalid input. Defaulting to 3 students.")
                    preview_limit = 3
            else:
                print("⚠️ Invalid choice. Defaulting to 3 students.")
                preview_limit = 3

            # Display formatted data
            print("\n📊 Preview of loaded data:")
            for section, students in data.items():
                print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"📘 Section: {section} ({len(students)} students)")
                print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"{'ID':<10} {'Name':<25} {'Quizzes':<30} {'Midterm':<10} {'Final':<10} {'Attendance':<10}")
                print("-" * 95)

                subset = students if preview_limit is None else students[:preview_limit]
                for s in subset:
                    name = f"{s['last_name']}, {s['first_name']}"
                    quizzes = ", ".join(str(q) if q is not None else "-" for q in s['quizzes'])
                    print(f"{s['student_id']:<10} {name:<25} {quizzes:<30} {s['midterm']:<10} {s['final']:<10} {s['attendance']:<10}")

            if preview_limit is not None:
                print(f"\n(📋 Showing only first {preview_limit} students per section.)")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")



# ===================================== #
# transform.py
# ===================================== #

def array_operations_menu():
    """Menu for array-level operations — transforming and viewing student data."""
    global data

    while True:
        print("\n--- Array Operations Menu ---")
        print("1) Compute final and letter grades (transform data)")
        print("2) View transformed sample records")
        print("3) Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if not data:
                print(" No data available. Please perform 'Clean ingest' first.")
                continue

            print("\n Transforming data using config.json ...")

            try:
                # Load configuration settings safely
                config = transform.load_config("config.json")

                if not config:
                    print(" Config file is empty or invalid.")
                    continue

                # Apply transformation section by section
                for section, students in data.items():
                    try:
                        data[section] = transform.transform(students, config)
                    except Exception as e:
                        print(f" Error transforming section '{section}': {e}")

                print("✅ Transformation complete! Weighted and letter grades have been computed.")

            except FileNotFoundError:
                print("⚠️ 'config.json' not found! Please make sure it exists in the directory.")
            except json.JSONDecodeError:
                print("⚠️ 'config.json' has invalid format. Please fix the JSON syntax.")
            except Exception as e:
                print(f"⚠️ Unexpected error during transformation: {e}")

        elif choice == "2":
            if not data:
                print("⚠️ No transformed data to view. Please run option 1 first.")
                continue

            print("\n📊 Preview of transformed data:")
            for section, students in data.items():
                print(f"\nSection: {section} — {len(students)} students")

                # Let user choose how many students to display
                mode = input("Show (1) all students or (2) a number of students? ").strip()

                if mode == "1":
                    sample_students = students
                elif mode == "2":
                    try:
                        num = int(input("How many students to display? "))
                        sample_students = students[:num]
                    except ValueError:
                        print("⚠️ Invalid number. Showing 3 by default.")
                        sample_students = students[:3]
                else:
                    print("⚠️ Invalid choice. Showing 3 by default.")
                    sample_students = students[:3]

                for s in sample_students:
                    print(f"  {s.get('student_id', '?')} | "
                          f"{s.get('last_name', '?')}, {s.get('first_name', '?')} | "
                          f"Final: {s.get('final_grade', 'N/A')} | "
                          f"Grade: {s.get('letter_grade', 'N/A')} | "
                          f"Remarks: {s.get('remarks', 'N/A')}")

            print("\n✅ End of preview.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# ===================================== #
# analyze.py
# ===================================== #

def analytics_menu():
    """Menu for analytics operations"""
    global data, config
    while True:
        print("\n--- Analytics Menu ---")
        print("1) Compute weighted grades")
        print("2) Compute distributions")
        print("3) Compute percentiles")
        print("4) Identify outliers")
        print("5) Analyze improvements")
        print("6) Back to Main Menu")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("Computing weighted grades...")
            try:
                for record in data:
                    quiz_avg = record.get("quiz_avg")
                    final = record.get("final")
                    midterm = record.get("midterm")
                    attendance = record.get("attendance")
                    weighted = analyze.weighted_mean(quiz_avg, final, midterm, attendance, config)
                    record["weighted_grade"] = weighted
                print("✅ Weighted grades computed and added to data.")
            except Exception as e:
                print(f"⚠️ Error computing weighted grades: {e}")

        elif choice == "2":
            print("Computing distributions...")
            # TODO: analyze.compute_distributions(data)
        elif choice == "3":
            print("Computing percentiles...")
            # TODO: analyze.compute_percentiles(data)
        elif choice == "4":
            print("Identifying outliers...")
            # TODO: analyze.detect_outliers(data)
        elif choice == "5":
            print("Analyzing improvements...")
            # TODO: analyze.compute_improvements(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


# ===================================== #
# reports.py
# ===================================== #

def reports_menu():
    """Menu for reporting and exports"""
    while True:
        print("\n--- Reports Menu ---")
        print("1) Print summary")
        print("2) Export per-section CSVs")
        print("3) Generate 'at-risk' lists")
        print("4) Back to Main Menu")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("Printing summary report...")
            # TODO: reports.print_summary(data)
        elif choice == "2":
            print("Exporting per-section CSVs...")
            # TODO: reports.export_section_csv(data, out_dir)
        elif choice == "3":
            print("Generating 'at-risk' list...")
            # TODO: reports.generate_at_risk_list(data, threshold)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")




# ===================================== #
# config.json
# ===================================== #

def configuration_menu():
    """Menu for configuration settings"""
    global config
    while True:
        print("\n--- Configuration Menu ---")
        print("1) Reload JSON config (weights, thresholds, folder paths)")
        print("2) Edit and save JSON config")
        print("3) Back to Main Menu")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
                with open("config.json", "r") as f:
                    config = json.load(f)
                print("✅ Config reloaded successfully.")
            except Exception as e:
                print(f"⚠️ Error reloading config: {e}")
        elif choice == "2":
            print("Editing and saving configuration...")
            # TODO: config.edit_and_save('config.json')
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


# ===================================== #
# PROGRAM START // time
# ===================================== #

if __name__ == "__main__":
    start_time = time.time()
    if check_required_files():
        load_startup_files()
        main_menu()
    else:
        print("❌ Startup aborted due to missing files.")
    end_time = time.time()
    print(f"\nProgram completed in {end_time - start_time:.2f} seconds.")
