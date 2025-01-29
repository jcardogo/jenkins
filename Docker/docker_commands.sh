sudo chown $USER:$USER /var/run/docker.sock
docker images #to list all images on server
docker run #to run images 
docker pull jenkins/jenkins #Pull jenkins image 
docker run -d -p 8080:8080 jenkins/jenkins #Starting jenkins container
docker ps #List all docker processes
docker exec -it <container-id> /bin/bash #access docker container shell
