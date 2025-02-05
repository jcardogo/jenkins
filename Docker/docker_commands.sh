sudo chown $USER:$USER /var/run/docker.sock
docker images #to list all images on server
docker run #to run images 
docker pull jenkins/jenkins #Pull jenkins image 
docker run -d -p 8080:8080 jenkins/jenkins #Starting jenkins container
docker ps #List all docker processes
docker exec -it <container-id> /bin/bash #access docker container shell
docker contaner ls #list all containers runing 
#deploy jenkins/jenkins image
docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk17
#Create a network
docker network create jenkins

#To run docker commands inside Jenkins node:
#1)DOwnload and run docker:dind
docker run \
  --name jenkins-docker \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind \
  --storage-driver overlay2

#2)Run my_jenkins_blueocean
docker run \
    --name jenkins-blueocean \ 
    --restart=on-failure \
    --detach \
    --network jenkins \
    --env DOCKER_HOST=tcp://docker:2376 \
    --env DOCKER_CERT_PATH=/certs/client \
    --env DOCKER_TLS_VERIFY=1 \
    --publish 8080:8080 \
    --publish 50000:50000 \
    --volume jenkins-data:/var/jenkins_home \
    --volume jenkins-docker-certs:/certs/client:ro \
    myjenkins-blueocean:0.0.1

#Deploy a nginx container to host a website
docker pull nginx
docker run -d -p 8083:80  -v /home/acardogo/Documents/GitHub/Website-Templates/reveal/:/usr/share/nginx/html nginx
#Deploy a apache httpd container to host a website 
docker pull httpd
docker run -d -p 8082:80  -v /home/acardogo/Documents/GitHub/Website-Templates/speed-hosting-bootstrap-free-html5-template/:/usr/local/apache2/htdocs/ httpd
