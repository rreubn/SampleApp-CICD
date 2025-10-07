pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/rreubn/SampleApp-CICD.git'
        BRANCH = 'main'
        // If you add GitHub credentials in Jenkins, put the ID here
        // GIT_CREDS = 'your-credential-id'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                echo "Cloning GitHub repository..."
                // Use credentialsId: GIT_CREDS if you added GitHub PAT
                git branch: "${BRANCH}", url: "${REPO_URL}" 
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python and dependencies..."
                // Install Python and pip inside Jenkins container
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
                // Make sure you have a tests/ folder or adjust accordingly
                sh '''
                    if [ -d "tests" ]; then
                        python3 -m pytest tests/
                    else
                        echo "No tests folder found, skipping tests."
                    fi
                '''
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
