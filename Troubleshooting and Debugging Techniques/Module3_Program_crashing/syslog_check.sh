date #check current date on the server
ls -lt /var/log/ | head #check recent changes on the files contained on /var/log/
tail sylog #to check latest logs on syslog file
sudo netstat -nlp | grep :80 #which will give us information about our network connections depending on the flags we pass (should be run on sudo mode), -n (numerical addesses) -l (listening sockets) -p (process ID)
ls -l /etc/nginx/sites-enabled/ #check configuration file for a specific site
nano <webpagesname> 
ls -l /etc/uwsgi/ #Check a related application for the webserver 
sudo nano /srv/site.example.com/prod.py 
sudo service uswsgi reload #To relaunch the service expecting to see logs
###Reload the pages and read the error message 


###Segmentation fault
ulimit -c unlimited # to dump a core file 
./example #calling the program to dump a core file 
gdb -c core example #to debug the core file from example program
backtrace #this command run over gdb will show the failing funciton and secuencially all the functions calling to it 
up #we can call "up" option to navigate further oin the backtrace-gdb until fefind the failing section
list #will list the lines surrounding failing function
print i #after identifying a specific variable that could cause the problem we can check some values 
print argv[0] #to check one element that interact with the variable to find why it fails 

