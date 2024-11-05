#this script will capitalize first character of each word
for i in $(cat story.txt); do B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; echo -n "${B}${i:1} "; done; echo -e "\n"
#this scrypt is working but it is more dificult to understand its purpose and test it