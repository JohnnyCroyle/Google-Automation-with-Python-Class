
import os


#print(os.getcwd())  # Get the current working directory
#print(os.listdir())  # List all files and directories in the current directory



outputs = {}
outputs['current_directory_before'] = os.getcwd()

print("Current working directory:", outputs['current_directory_before'])

outputs['files_in_directory_before'] = os.listdir()

print("Files in current directory before creating new file:", outputs['files_in_directory_before'])

outputs['path_value'] = os.environ.get('PATH')
print("PATH environment variable:", outputs['path_value'])
