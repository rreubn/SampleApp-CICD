pipeline {
    agent any

    environment {
        PYTHON = "python3"
    }

    stages {

        stage('Checkout SCM') {
            steps {
                // Pull code from GitHub main branch
                git branch: 'main', url: 'https://github.com/rreubn/SampleApp-CICD.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                    ${PYTHON} -m pip install --upgrade pip
                    ${PYTHON} -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running automated tests..."
                sh '''
                    ${PYTHON} -m pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Simulated deployment: Deployment successful!"
                // In real scenario, you could deploy to cloud (AWS, Heroku, etc.)
            }
        }

    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "All stages completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check console output for errors."
        }
    }
}
