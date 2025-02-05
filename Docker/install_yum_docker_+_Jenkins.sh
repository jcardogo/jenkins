#! /bin/bash

sudo yum update -y
sudo yum install -y docker 
sudo systemctl start docker
sudo systemctl enable docker
#Install Jenkins
sudo chown $USER:$USER /var/run/docker.sock
docker pull jenkins/jenkins
docker run -d -p 8080:8080 jenkins/jenkins