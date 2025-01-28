#! /bin/bash

#Confirm git is installed
git --version
#Create a new directory por your project
mkdir /home/acardogo/Documents/projects/AWS/ #replace with path to your project
cd /home/acardogo/Documents/projects/AWS/ #replace with path to your project
git init #Initialize the project creating a .git file on the directory
#Update the URL: to incluide your token
#export GITHUB_TOKEN="11ARKP55Y0zQ3UaSXx4KtE_F0iZXJOicLtjvM9XuuQPuel8Skrz3d2AMhtbv0dPS3hMOY4ZHG5nPKiOSJu" #Replace with the current GitHub PAT token
git remote add origin https://jcardogo:$GITHUB_TOKEN@github.com/jcardogo/AWS.git
git remote set-url origin https://jcardogo:$GITHUB_TOKEN@github.com/jcardogo/AWS.git
#Manipulate files
touch README.md #Create a readmy file to add details about the project
echo "# My project" >> README.md #Populate README.md file with initial line
git add . #Add all files to the repository
git commit -m "Initial commit" #Commit the added files including the commit comment
git push origin main 
git fetch