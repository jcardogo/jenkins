pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'my_webpage'
        DOCKER_CONTAINER_NAME = 'my-nginx-container'
        GIT_REPO_URL = 'https://jcardogo:$GITHUB_PAT@github.com/jcardogo/AlejandroCardoso_website.git'
        
        // AWS environment variables
        AWS_CREDENTIALS_ID = 'aws-credentials-id'
        AWS_REGION = 'us-east-1'
        AWS_INSTANCE_ID = '....'

        // Azure environment variables
        AZURE_CREDENTIALS_ID = 'azure-credentials-id'
        AZURE_RESOURCE_GROUP = 'your-resource-group'
        AZURE_VM_NAME = '<your -azure-vm-name>'

        //GCP environment variables
        GCP_CREDENTIALS_ID = 'gcp-credentials-id'
        GCP_PROJECT_ID = 'your-gcp-project-id'
        GCP_ZONE = 'us-central1-a'
        GCP_INTANCE_NAME = '<your-gcp-vm-name>'

    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url "${env.GIT_REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE_NAME}").inside {
                        sh 'echo "FROM nginx:latest" > Dockerfile'
                        sh 'docker build -t ${DOCKER_CONTAINER_NAME} .'
                    }
                }
            }
        }

        // stage ('Deploy to AWS EC2') {
        //     steps {
        //         withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDENTIALS_ID]]) {
        //             script {
        //                 sh """
        //                 ssh -i /path/to/your/aws/key.pem ec2-user@${env.AWS_INSTANCE_ID} 'docker run -d --name ${env.DOCKER_CONTAINER_NAME} -p 80:80 ${env.DOCKER_IMAGE_NAME}'
        //                 """
        //             }
        //         }    
        //     }
        // }

        // stage('Deploy to Azure VM') {
        //     steps {
        //         withCredentials([azureServicePrincipal(credentialsId: env.AZURE_CREDENTIALS_ID)]) {
        //             script {
        //                 sh """
        //                 ssh azureuser@${env.AZURE_VM_NAME}.${env.AZURE_RESOURCE_GROUP}.cloudapp.azure.com 'docker run -d --name ${env.DOCKER_CONTAINER_NAME} -p 80:80 ${env.DOCKER_IMAGE_NAME}'
        //                 """
        //             }
        //         }
        //     }
        // }

        // stage('Deploy to GCP VM') {
        //     steps {
        //         withCredentials([file(credentialsId: env.GCP_CREDENTIALS_ID, variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
        //             script {
        //                 sh """
        //                 gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
        //                 gcloud compute ssh ${env.GCP_INSTANCE_NAME} --zone=${env.GCP_ZONE} --command='docker run -d --name ${env.DOCKER_CONTAINER_NAME} -p 80:80 ${env.DOCKER_IMAGE_NAME}'
        //                 """
        //             }
        //         }
        //     }
        // }

        stage ('Run Docker Container') {
            steps {
                sh 'docker run -d --name ${DOCKER_CONTAINER_NAME} || true'
                sh 'docker rm ${DOCKER_CONTAINER_NAME} || true'
                sh 'docker rmi ${DOCKER_IMAGE_NAME} || true'
            }
        }

        stage('Wait for One Hour') {
            steps {
                script {
                    sleep(time: 1, unit: 'HOURS')
                }
            }
        }

        stage ('Cleanup') {
            steps {
                script {
                    sh 'docker stop ${DOCKER_CONTAINER_NAME} || true && docker rm ${env.DOCKER_CONTAINER_NAME}"' 
                    // withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDENTIALS_ID]]) {
                    //     sh 'ssh -i /path/to/your/aws/key.pem ec2-user@${env.AWS_INSTANCE_ID} "docker stop ${env.DOCKER_CONTAINER_NAME} && docker rm ${env.DOCKER_CONTAINER_NAME}"'
                    // }
                    // withCredentials([azureServicePrincipal(credentialsId: env.AZURE_CREDENTIALS_ID)]) {
                    //     sh 'ssh azureuser@${env.AZURE_VM_NAME}.${env.AZURE_RESOURCE_GROUP}.cloudapp.azure.com "docker stop ${env.DOCKER_CONTAINER_NAME} && docker rm ${env.DOCKER_CONTAINER_NAME}"'
                    // }
                    // withCredentials([file(credentialsId: env.GCP_CREDENTIALS_ID, variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    //     sh 'gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS} && gcloud compute ssh ${env.GCP_INSTANCE_NAME} --zone=${env.GCP_ZONE} --command="docker stop ${env.DOCKER_CONTAINER_NAME} && docker rm ${env.DOCKER_CONTAINER_NAME}"'
                    // }
                }
            }
        }
    }

    port {
        always {
            script {
                sh 'docker stop ${DOCKER_CONTAINER_NAME} || true'
                sh 'docker rm ${DOCKER_CONTAINER_NAME} || true'
                sh 'docker rmi ${DOCKER_IMAGE_NAME} || true'
            }
        }
    }
}