/import_data$ cat contacts.csv | ./import.py --server test



/import_data$ wc -l contacts.csv # will print the amount of lines in a file 



/import_data$ head -15 contacts.csv #print the first lines of the file



/import_data$ tail -20 contacts.csv #print last 15 lines of the file 


/import_data$ head -50 contacts.csv | ./import.py --server test 


/import_data$ head -50 contacts.csv | head -25 | ./import.py --server test #apply the first 25 of the first 50 lines of the contacts.csv file into import.py 


/import_data$ head -50 contacts.csv | tail -25 | ./import.py --server test


/import_data$ head -50 contacts.csv | tail -25 | head -13 | ./import.py --server test


/import_data$ head -50 contacts.csv | tail -25 | tail -12 | head -6 | ./import.py --server test


/import_data$ head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3 


/import_data$ cat contacts.csv | ./import.py --server test