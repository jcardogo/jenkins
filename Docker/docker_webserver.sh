#!/bin/bash

#configuration
DOCKER_IMAGE_NAME="my-nginx-web"
DOCKER_CONTAINER_NAME="my-web-container-nginx"
GITHUB_REPO_URL="https://jcardogo:$GITHUB_PAT@github.com/jcardogo/AlejandroCardoso_website.git"
GITHUB_BRANCH="master"
HTML_DIR="html"
LOCAL_REPO_DIR="/home/acardogo/Documents/projects/containers"
LOCAL_DOCKERFILE_DIR="/home/acardogo/Documents/projects/docker_context" #local directory to build the docker container from.
LOCAL_PORT=8086 #port to map the container to

#Cleanup from previous runs
echo "Cleaning up..."
sudo docker stop "$DOCKER_CONTAINER_NAME" 2>/dev/null || true #ignore error if container is not running
sudo docker rm "$DOCKER_CONTAINER_NAME" 2>/dev/null || true #ignore error if container does not exist
#rm -rf "$LOCAL_REPO_DIR"
#rm -rf "$LOCAL_DOCKERFILE_DIR"

#Clone the GitHub repository
echo "Cloning GitHub repository..."
git clone --branch "$GITHUB_BRANCH" "$GITHUB_REPO_URL" "$LOCAL_REPO_DIR"

#Create Docker build context directory
echo "Creating Docker build context ...."
mkdir "LOCAL_DOCKERFILE_DIR"
cp -r "$LOCAL_REPO_DIR/$HTML_DIR" "$LOCAL_DOCKERFILE_DIR"

#Create Dockerfile
echo "Creating Dockerfile..."
cat <<EOF > "$LOCAL_DOCKERFILE_DIR/Dockerfile"
FROM nginx:alpine
COPY . /usr/share/nginx/html/
EXPOSE 80
EOF

#Build Docker image
echo "Building Docker image..."
sudo docker build -t "$DOCKER_IMAGE_NAME" "$LOCAL_DOCKERFILE_DIR"

#Run Docker container
echo "Running Docker container..."
sudo docker run -d -p "$LOCAL_PORT:80" --name "$DOCKER_CONTAINER_NAME" "$DOCKER_IMAGE_NAME"  #run the container in detached mode 

#Verify deployment (Simple curl check)
echo "Verifying deployment..."
sleep 5 #wait for the container to start
curl "http://localhost:$LOCAL_PORT" | grep "Hello World" #check if the website is up and running
if [ $? -eq 0 ]; then
    echo "Deployment successful!"
else
    echo "Deployment failed!"
fi
#EOF

#Cleanup (Optional - remove cloned repo and Docker build context)
echo "Cleaning up cloned repo and docker buils context..."
rm -rf "$LOCAL_REPO_DIR"
rm -rf "$LOCAL_DOCKERFILE_DIR"

echo "Decployment complete."