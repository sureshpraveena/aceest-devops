pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/sureshpraveena/aceest-devops.git'
            }
        }

        stage('Python Setup & Test') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root'   // 👈 fixes permission issue
                }
            }
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-devops:latest .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'docker-creds') {
                        sh '''
                        docker tag aceest-devops:latest kspraveena92/aceest-devops:latest
                        docker push kspraveena92/aceest-devops:latest
                        '''
                    }
                }
            }
        }
    }
}