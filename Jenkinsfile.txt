pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rreubn/SampleApp-CICD.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment successful! (Simulated for now)'
            }
        }
    }
}
