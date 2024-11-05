#!/bin/bash

n=0
command=$1 #command "$" is similar to sys.argv[1]
while ! $command && [ $n -le 5 ]; do 
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;