import subprocess
#subprocess.run(["date"],shell=True)
#subprocess.run(["sleep", "2"],shell=True)
result = subprocess.run(["ls", "this_file_does_not_exist"],shell=True)
print(result.returncode)