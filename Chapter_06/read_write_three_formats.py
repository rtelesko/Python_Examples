import csv
import json


def read_text_file(filename):
    print("Reading from text file:")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f]
            for line in lines:
                print(line)
        return lines
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
    print("-" * 40)
    return None


def write_text_file(filename, lines):
    print("Writing to text file:")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")
    print("-" * 40)


def read_csv_file(filename):
    print("Reading from CSV file:")
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            for row in rows:
                print(row)
        return rows
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
    print("-" * 40)
    return None


def write_csv_file(filename, rows):
    print("Writing to CSV file:")
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")
    print("-" * 40)


def read_json_file(filename):
    print("Reading from JSON file:")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(json.dumps(data, indent=4))
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
    print("-" * 40)
    return None


def write_json_file(filename, data):
    print("Writing to JSON file:")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")
    print("-" * 40)


if __name__ == "__main__":
    # Read existing files
    txt_data = read_text_file("sample.txt")
    csv_data = read_csv_file("sample.csv")
    json_data = read_json_file("sample.json")

    # Write new example files
    write_text_file("output.txt", ["Line 1", "Line 2", "Line 3"])
    write_csv_file("output.csv", [["Name", "Age"], ["Alice", 30], ["Bob", 25]])
    write_json_file("output.json", {"employees": [{"name": "Eve", "role": "Intern"}]})
