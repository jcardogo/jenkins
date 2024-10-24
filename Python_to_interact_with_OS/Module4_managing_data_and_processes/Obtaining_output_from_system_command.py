import subprocess

#####Section 1
result = subprocess.run(["host", "8.8.8.8"], capture_output=True) #adding the "capture_output=True" parameter

result = subprocess.run(["host", "8.8.8.8"], capture_output=True) 
print(result.returncode)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split()) #decoding the bit 

#####Section 2

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)


import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
