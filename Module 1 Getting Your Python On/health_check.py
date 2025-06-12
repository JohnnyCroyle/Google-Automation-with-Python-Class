import shutil
import psutil



def check_disk_space(disk):
    du = shutil.disk_usage(disk)
    free_space = du.free / du.total * 100  # Calculate free space percentage
    return free_space > 20  # Check if free space is less than 30%

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)

 #   print(cpu_usage)
    return cpu_usage < 75  # Check if CPU usage is less than 75%

#print(check_disk_space('/'))
#print(check_cpu_usage())

if not check_disk_space('/')  or not check_cpu_usage():
    print("ERROR!")
else:
    print("OK!")

