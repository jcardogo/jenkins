#Installing Jenkins on Rocky Linux 8 https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos
sudo yum install wget -y # Install wget 
sudo wget -O /etc/yum.repos.d/jenkins.repo     https://pkg.jenkins.io/redhat-stable/jenkins.repo # Add the Jenkins repository
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key # Import the key
sudo yum upgrade -y # Upgrade all packages
# Add required dependencies for the jenkins package
sudo yum install fontconfig java-17-openjdk -y # Install the Jenkins package
sudo yum install jenkins -y # Install Jenkins
sudo systemctl daemon-reload # Reload the systemd configuration
sudo systemctl start jenkins # Start Jenkins
sudo firewall-cmd --add-port=8080/tcp --permanent # Open the firewall port
sudo reboot # Reboot the system

##Unlock Jenkins
java -jar jenkins-cli.jar unlock

##Connecting jenkins via CLI
export JENKINS_URL=http://localhost:8080
java -jar jenkins-cli.jar login --username your_username --password yourpassword

##Configuring jenkins via CLI
##Create a job
java -jar jenkins-cli.jar create-job my_job < config.xml
java -jar jenkins-cli.jar update-job my_job < config.xml
##Delete a job
java -jar jenkins-cli.jar delete-job my_job
java -jar jenkins-cli.jar list-jobs
##Get job
java -jar jenkins-cli.jar get-job my_job > config.xml
