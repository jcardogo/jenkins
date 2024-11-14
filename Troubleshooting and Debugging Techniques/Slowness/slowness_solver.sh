top #sort the processes using most cpu time, or sorted by memory the ones most using memory
iotop #disk usage
iftop #network band wigth 
#a cache stores data in a form that's faster to access than its original form.
1) starting slowly, check the application programmed to start in boot
2) a program using much of the RAM (Random Allocation Memory)
3) when the files on sidk are soo large it is so demanding to access the files 
4) Check if only some users are affected, 
5) read and write to a shared file system on external server
6) disk overloaded 
RESOURCES:
- CPU (Processing Unit)
- RAM (Random Allocation Memory)
- Storage (Long term repository for files)
- Graphic Processor ()
SLOW WEB SERVER
ab -n 500 site.com #stands for Apache Benchmark tool to figure out how slow it is. We'll run ab -n 500 to get the average timing of 500 requests, result of 150 miliseconds average is not good so we investigate further
top # we can identofy processes runing, in example case we can see multiple ffmeg using most of CPU #%CPU usage is the use on a single minute 100% meaning that the processing unit is busy ahole minute with no resto a ttend any extra request
#We can configure process piority (lower the number higher the priority)
nice # to define the priority of a starting process
renice #to change the piority of a currently runing process 
pidof #receives the process name and returns all the process IDs that have that name
for pid in $(pidof ffmpeg); do renice 19 $pid; done #this command would change the priority of ffmeg named processes to lowest priority iterating one by one over pidof list
ps ax | less #will show us all the processes runing on our computer, using less to scroll through it
/ffmpeg # "/" is the search toll on less to find ffmpeg process 
#output show the nature and purpose of the processes, in this case video files convertion, we need now to know where those files are located
locate static/001.webm #this command would search for the file 
#then from located path we search for any file calling ffmpeg process
grep ffmpeg * #this command will show any mention of the process name on files 
#as we found the root cause as deamonize call on a file is triggering all processes simultaneusly we remove that part to avoid that vehavior and instead run each convertion one at the time
killall -STOP ffmpeg #This command will pause all ffmpeg processes 
for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done #to triger each process on pidof ffmpeg list to continue until it completes and then trigger next until complete all existing processes 
#this solution now is showing 33 miliseconds as mean time for 500 request  
###########################
time ./send_reminders.py "2020-01-13|Example|test1" #used to show the time used to complete the script (Real 0,129s; user 0,06; sys 0,013) 
#we want to find a profiler to improve the code 
pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9" #this will generate a file "profile.out" 
kcachegrind profile.out #to see graphically the chart of function and methods insteraction, in example case pointing to send_remainders.py method
atom send_remainders.py








 