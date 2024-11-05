cut -d' ' -f5- /var/log/messages | sort | uniq -c | sort -nr | head #comand to be used on centos 
#cut -d' ' -f5- /var/log/messages | sort | uniq -c | sort -nr | head #command to be used on ubuntu

# "tail" is listing the content of the file "/var/log/messages"
# "cut-d" to use cut as a delimiter
# "-f5-" to list from the line number 5 and after avoinding to use tha headlines and dates
# "sort" will sort the lines alfabetically
# "uniq -c" will identify each unique string mentioned and count the repetitions
# "sort -nr" will sort the number of repetitions in reversed orden from larger to shorter
# "head" will print first 10 lines with mos repited actions and the number of repetitions

