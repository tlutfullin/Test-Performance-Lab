import json
import sys

def load_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading file {file_path}: {e}")
        sys.exit(1)

def save_json_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred while writing to file {file_path}: {e}")
        sys.exit(1)

def build_value_dict(values):
    value_dict = {}
    try:
        for item in values:
            if "id" in item and "value" in item:
                value_dict[item["id"]] = item["value"]
            else:
                raise ValueError("Invalid format in values data")
        return value_dict
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while building value dictionary: {e}")
        sys.exit(1)

def fill_values(test_structure, value_dict):
    try:
        if "id" in test_structure:
            test_id = test_structure["id"]
            if test_id in value_dict:
                test_structure["value"] = value_dict[test_id]

        if "values" in test_structure:
            for sub_test in test_structure["values"]:
                fill_values(sub_test, value_dict)
    except Exception as e:
        print(f"An unexpected error occurred while filling values: {e}")
        sys.exit(1)

def main(values_file, tests_file, report_file):
    values_data = load_json_file(values_file)
    tests_data = load_json_file(tests_file)

    if "values" not in values_data or "tests" not in tests_data:
        print("Error: Invalid format in input files")
        sys.exit(1)

    value_dict = build_value_dict(values_data["values"])
    for test in tests_data["tests"]:
        fill_values(test, value_dict)

    save_json_file(report_file, tests_data)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)
