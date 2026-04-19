pipeline {
    agent any
    stages {
        stage('Clone code') {
            steps {
                git 'https://github.com/sureshpraveena/aceest-devops'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest tests'
            }
        }
            stage('Build Docker image') {
                steps {
                    sh 'docker build -t aceest:v2 .'
                }
            }
    }
}