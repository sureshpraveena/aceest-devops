pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-devops:${BUILD_NUMBER} .'
            }
        }
    }
}