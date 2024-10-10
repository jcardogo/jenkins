#!/usr/bin/env python
import shutil #module to get important information about the machine 
import psutil #module to get information about processor

def check_disk_usage(disk): #Function that accepts "disk" identification to process it  
    du = shutil.disk_usage(disk) #defining "du" as a variable that represent the disk usage
    free = du.free /  du.total * 100 #calculating the variable free as a float betwen 0 and 100
    return free > 20 #returniing boolean TRUE when the usage when the free disk storage space is more than 20%

def check_cpu_usage(): #Function
    usage = psutil.cpu_percent(1) #defining usage variable as a float average of cpu percentage used from last 1 second time period
    return usage < 75 #Returning boolean TRUE when cpu usage is less than 75%

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everithing is OK!")

######this code was created on dos codemode so to run it on unix i had to use this command on the linux machine "dos2unix health_checks.py"