import json

# A dictionary is a Python data structure in memory,
# while JSON is a text format used to store or exchange structured data.

# Create a Python dictionary
person = {
    "name": "Alice",
    "age": 30,
    "student": False
}

# json.dumps() and json.loads() convert between Python data and JSON text

# Convert the Python dictionary into JSON text
json_text = json.dumps(person)

print("JSON:")
print(json_text)

# Show the data type
print(type(json_text))   # <class 'str'>


# Convert the JSON text back into a Python dictionary
try:
    person_again = json.loads(json_text)
    print(person_again)

    # Show the data type
    print(type(person_again))   # <class 'dict'>

except json.JSONDecodeError as error:
    print("JSON parsing error:", error)