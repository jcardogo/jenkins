#!/bin/bash

git clone --branch master https://jcardogo:$GITHUB_PAT@github.com/jcardogo/AlejandroCardoso_website.git /home/acardogo/Documents/projects/containers #clone the repository

mkdir "/home/acardogo/Documents/projects/docker_context" #create a directory to build the docker container from
cp -r /home/acardogo/Documents/projects/containers/* /home/acardogo/Documents/projects/docker_context #copy the html files to the directory

#create a Dockerfile
cat <<EOF > "/home/acardogo/Documents/projects/docker_context/Dockerfile" 
FROM nginx:alpine 
COPY . /usr/share/nginx/html/
EXPOSE 80
EOF


sudo docker build -t "my-nginx-web" "/home/acardogo/Documents/projects/docker_context" #build the docker image

sudo docker run -d -p "8086:80" --name "my-web-container-nginx" "my-nginx-web" #run the container in detached mode

rm -rf /home/acardogo/Documents/projects #cleanup

sleep 5 #wait for the container to start

sudo docker stop my-web-container-nginx #stop the container
sudo docker rm my-web-container-nginx #remove the container
sudo docker rmi my-nginx-web #remove the image
