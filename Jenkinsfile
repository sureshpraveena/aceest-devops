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

        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                // sh 'docker build -t aceest-devops:latest . || true'
                sh 'docker build -t aceest-devops:latest .'
            }
        }
    }
}