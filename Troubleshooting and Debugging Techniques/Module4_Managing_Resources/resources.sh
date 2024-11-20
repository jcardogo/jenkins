#CPU
top
#Memory
python3 -m memory_profiler contents_stats_simple.py #create a profile of memory used by the method
top #colums VIRT(all memory allocated for each process) *RES* (Dynamic memory allocated for each process) SHR (memory shared across processes)
#Disk
sudo lsof | grep deleted #look for the currently open files filtering for deleted ones
#Network
iftop
