pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                echo "Cloning GitHub repository..."
                git branch: 'main', url: 'https://github.com/rreubn/SampleApp-CICD.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python and dependencies..."
                sh '''
                    apt-get update -y
                    apt-get install -y python3 python3-pip
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running automated tests..."
                sh 'python3 -m pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo "Simulated deployment: Deployment successful!"
            }
        }

    }

    post {
        always { echo "Pipeline finished." }
        success { echo "All stages completed successfully!" }
        failure { echo "Pipeline failed. Check console output for errors." }
    }
}
