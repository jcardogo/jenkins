###Balance on workloads on a computer
Split the work in processes
    CPU processing time
    Networ IO
    Disk IO 
#Threads let us run parallel tasks inside a process. 
'''
In Python, we can use the Threading or AsyncIO modules to do this. These modules let us specify which parts 
of the code we want to run in separate threads or as separate asynchronous events, and how we want the 
results of each to be combined in the end.

it might happen that all threads get executed in the same CPU processor. In that case, if you want to use more 
processors, you'll need to split the code into fully separate processes. 

I/O bound: script waiting for input or output
CPU bound: your script is executing operations in parallel consuming all CPU time

Data management options
csv file
SQLite: lightweight database system that lets you query the information stored in the file without needing to run a database server
Fully-fledged DataBase server: for medium size data 
dynamic cache service like memcached:  keeps the most commonly used results in RAM to avoid querying the database unnecessarily

'''
Use case on web ser

Activity Monitor: Mac OS tool that shows what's using the most CPU, memory, energy, disk, or network

Cache: This stores data in a form that's faster to access than its original form

Executor: This is the process that's in charge of distributing the work among the different workers

Expensive actions: Actions that can take a long time to complete

Futures: A module provides a couple of different executors, one for using threads and the other one for using processes

Lists: Sequences of elements

Memory leak: This happens when a chunk of memory that's no longer needed is not released

Profiler: A tool that measures the resources the code is using to see how the memory is allocated and how the time is spent

Real time: The amount of actual time that it took to execute the command

Resource Monitor (or Performance Monitor): Windows OS tool that shows what's using the most CPU, memory, energy, disk, or network

Sys time: The time spent doing system level operations

Threads: Run parallel tasks inside a process

User time: The time spent doing operations in the user space


