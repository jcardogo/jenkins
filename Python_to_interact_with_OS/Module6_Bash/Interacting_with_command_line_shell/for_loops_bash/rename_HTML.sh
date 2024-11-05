#!/bin/bash
#before executing this on system is a good practice to run echo_rename_HTML.sh to confirm if this is the expected behavior and then execute this
for file in *.HTM; do
        name=$(basename "$file" .HTM) #the name use of "" arround the parameter file would allow us to define the parameter even if it contains blanc spaces
        mv "$file" "$name.html" 
done 