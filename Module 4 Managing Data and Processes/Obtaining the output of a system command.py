import subprocess

#result = subprocess.run(["host", "8.8.8.8"], capture_output=True,shell=True)


# result = subprocess.run(["host", "8.8.8.8"], capture_output=True,shell=True)
# print(result.returncode)



# result = subprocess.run(["host", "8.8.8.8"], capture_output=True,shell=True)
# print(result.stdout)



# result = subprocess.run(["host", "8.8.8.8"],shell=True, capture_output=True)
# print(result.stderr.decode().split())




# result = subprocess.run(["rm", "does_not_exist"], capture_output=True,shell=True)



# result = subprocess.run(["rm", "does_not_exist"], capture_output=True,shell=True)
# print(result.returncode)


result = subprocess.run(["rm", "does_not_exist"], shell=True,capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)