#TODO write script to combine each line in into one line seperated by a comma until it reaches a line that contains a line that says END OF LINE  and then start a new line and continue on
# import os
import re   
def process_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_line = []
        for line in infile:
            line = line.strip()
            if line == "END OF LINE":
                if current_line:
                    outfile.write(', '.join(current_line) + '\n')
                    current_line = []
            elif line:  # Only process non-empty lines
                current_line.append(line)
        # Write any remaining lines after the last "END OF LINE"
        if current_line:    
            outfile.write(', '.join(current_line) + '\n')

# Example usage
# 
#  


process_lines('c:\\Users\\johnn\\source\\repos\\Google Automation with Python Class\\Module 5 Testing in Python\\jobsearch.txt', 'c:\\Users\\johnn\\source\\repos\\Google Automation with Python Class\\Module 5 Testing in Python\\jobsearch_cleaned.txt')