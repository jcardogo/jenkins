#! /bin/bash

sudo apt-get update && sudo apt-get install apache2
sudo apt-get install docker 
sudo systemctl start docker
sudo systemctl enable docker
#Install Jenkins
sudo chown $USER:$USER /var/run/docker.sock
docker pull jenkins/jenkins
docker run -d -p 8080:8080 jenkins/jenkin
docker exec -it <CONTAINER-ID> /bin/bash #To access the container as terminal 


