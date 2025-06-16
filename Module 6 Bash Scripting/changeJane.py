# This script renames files listed in a text file by replacing 'jane' with 'jdoe' in their names.
# Usage: python rename_files.py file_list.txt   


import sys
import subprocess

with open(sys.argv[1], 'r') as file:
    old_names = file.readlines()


with open(sys.argv[1], 'r') as file:
    old_names = file.readlines()
for line in old_names:
    old_name = line.strip()
    new_name = old_name.replace('jane', 'jdoe')

    subprocess.run(['mv', old_name, new_name])







