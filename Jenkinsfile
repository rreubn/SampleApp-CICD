pipeline {
    agent {
        docker { image 'python:3.11' } // Run all stages inside Python 3.11 container
    }

    stages {

        stage('Checkout SCM') {
            steps {
                echo "Cloning GitHub repository..."
                git branch: 'main', url: 'https://github.com/rreubn/SampleApp-CICD.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running automated tests..."
                sh 'pytest tests/'
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
