pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Build Java code with Gradle
                
                sh 'gradle build'
            }
        }
        stage('Create Nginx Docker Container') {
            steps {
                // Create a Docker container from the Gradle build artifact
                sh 'docker build -t my-nginx-container .'
            }
        }
        stage('Save Artifact and Container') {
            steps {
                // Save the Gradle build artifact to a repository (e.g. Artifactory)
                sh 'curl -u username:password -X PUT http://artifactory-url.com/artifact/my-java-artifact.jar -T target/my-java-artifact.jar'
                // Save the Docker container to a repository (e.g. Docker Hub)
                sh 'docker tag my-nginx-container:latest username/my-nginx-container:latest'
                sh 'docker push username/my-nginx-container:latest'
            }
        }
        stage('Deploy to EC2 Instance') {
            steps {
                // Install the Docker container on an EC2 instance in AWS
                sh 'aws ec2 deploy --instance-id i-0123456789abcdef0 --docker-container username/my-nginx-container:latest --port 8080'
                // Expose port 8080 to the internet
                sh 'aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port 8080 --cidr 0.0.0.0/0'
            }
        }
    }
    post {
        // Send a notification if the pipeline fails
        failure {
            mail to: 'jcardogo@gmail.com',
                 subject: 'Jenkins Pipeline Failed',
                 body: 'The pipeline failed to deploy the application.'
        }
    }
}