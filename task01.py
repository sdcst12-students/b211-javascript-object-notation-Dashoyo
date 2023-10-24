#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

def find_largest_number(numbers):
    return max(numbers)

filename = ["task01a.txt", "task01b.txt", "task01c.txt"]

for file_name in filename:
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        
        largest_number = find_largest_number(data)
        
        print(f"The largest number in {file_name}: {largest_number}")
    
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON data in {file_name}.")
