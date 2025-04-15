pipeline {
    agent any
    environment {
        IMAGE_NAME = "qwen-coding-api"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        REGISTRY = "your-dockerhub-username"
    }
    stages {
        stage('Lint & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'flake8 src/'
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $REGISTRY/$IMAGE_NAME:$IMAGE_TAG .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $REGISTRY/$IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }
        stage('Deploy (docker-compose)') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
        }
        success {
            mail to: 'mlops-team@example.com', subject: 'Pipeline Success', body: 'Qwen Coding API pipeline completed!'
        }
        failure {
            mail to: 'mlops-team@example.com', subject: 'Pipeline Failed', body: 'Pipeline failed! Check Jenkins.'
        }
    }
}
