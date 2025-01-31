pipeline {
    agent any  // Run on any available agent

    stages {
        stage('Hello') {
            steps {
                echo 'Hello, Jenkins!'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building..."' // Example build step (replace with your actual build commands)
                // Or use specific build tools:
                // maven(mavenName: 'MyMaven', pom: 'pom.xml')
                // gradle(gradleName: 'MyGradle', tasks: 'build')
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."' // Example test step (replace with your actual test commands)
                // Example using JUnit:
                // junit('**/target/surefire-reports/*.xml')
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."' // Example deploy step (replace with your actual deploy commands)
                // Example using SSH:
                // sshpublisher publishers: [sshPublisher(configName: 'MySSHServer',...)]
            }
        }
    }
}