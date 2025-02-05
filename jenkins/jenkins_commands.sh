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
