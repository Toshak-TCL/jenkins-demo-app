pipeline {
    agent any

    environment {
        APP_SERVER = "clouduser@100.94.70.237"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Toshak-TCL/jenkins-demo-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo .'
            }
        }

        stage('Save Docker Image') {
            steps {
                sh 'docker save flask-demo > flask-demo.tar'
            }
        }

        stage('Copy Image To App Server') {
            steps {
                sh '''
                scp -o StrictHostKeyChecking=no \
                flask-demo.tar $APP_SERVER:/tmp/
                '''
            }
        }

        stage('Deploy On App Server') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no $APP_SERVER "
                    docker load < /tmp/flask-demo.tar &&
                    docker rm -f flask-demo-container || true &&
                    docker run -d -p 5000:5000 \
                    --name flask-demo-container flask-demo
                "
                '''
            }
        }
    }
}