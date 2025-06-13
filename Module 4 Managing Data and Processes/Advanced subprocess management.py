import os
import subprocess

my_env = os.environ.copy()

print("Original PATH:", my_env["PATH"])
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

print("Updated PATH:", my_env["PATH"])


result = subprocess.run(["myapp"], env=my_env, capture_output=True, text=True, shell=True)