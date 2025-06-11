import numpy as np
import re
import sys
import os # Added for better path checking

def analyze_numbers_in_file(input_filepath):
    """
    Reads numbers from a file, counts the occurrences of each digit (0-9),
    and returns a NumPy array with the counts.

    """
    if not os.path.exists(input_filepath):
        print(f"Error: Input file '{input_filepath}' not found.", file=sys.stderr)
        return None
    
    try:
        with open(input_filepath, "r") as file:
            content = file.read()
        
        numbers = content.split(' ')
        digits_count = np.zeros(10, dtype=int)
        
        for num_str in numbers:
            digit_groups = re.findall(r'\d', num_str)
            for digit_char in digit_groups:
                digits_count[int(digit_char)] += 1
        
        return digits_count
    except Exception as e: 
        print(f"An error occurred during file analysis: {e}", file=sys.stderr)
        return None

def generate_report_file(digits_array, output_filepath):

    if digits_array is None:
        print("Cannot generate report: No digit data provided.", file=sys.stderr)
        return False

    try:
        with open(output_filepath, "w") as file:
            for i, count in enumerate(digits_array):
                file.write(f"{i} {int(count)}\n")
        return True
    except Exception as e: 
        print(f"An error occurred while writing the report file: {e}", file=sys.stderr)
        return False