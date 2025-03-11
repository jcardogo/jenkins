#!/bin/bash

git clone --branch master https://jcardogo:$GITHUB_PAT@github.com/jcardogo/AlejandroCardoso_website.git ./containers #clone the repository

mkdir "./docker_context" #create a directory to build the docker container from
cp -r ./containers/* ./docker_context #copy the html files to the directory

#create a Dockerfile
cat <<EOF > "./docker_context/Dockerfile" 
FROM nginx:alpine 
COPY . /usr/share/nginx/html/
EXPOSE 80
EOF


sudo docker build -t "my-nginx-web" "./docker_context" #build the docker image

sudo docker run -d -p "8086:80" --name "my-web-container-nginx" "my-nginx-web" #run the container in detached mode

rm -rf ./containers #cleanup

#sleep 5 #wait for the container to start

#sudo docker stop my-web-container-nginx #stop the container
#sudo docker rm my-web-container-nginx #remove the container
#sudo docker rmi my-nginx-web #remove the image
