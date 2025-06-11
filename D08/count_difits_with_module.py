
import numpy as np
import re
import sys
import os 
from MyModule import generate_report_file,analyze_numbers_in_file 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python number_analyzer.py <input_filepath> <output_filepath>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f"Analyzing numbers from: {input_file}")
    
    digit_counts = analyze_numbers_in_file(input_file)

    if digit_counts is not None:
        print(f"Generating report to: {output_file}")
        generate_report_file(digit_counts, output_file)
    else:
        print("Analysis failed. Report not generated.")
    
    sys.exit(0)