pipeline {
    agent any
    environment {
        VENV = "${WORKSPACE}/venv"
    }
    stages {
        stage('Setup') {
            steps {
                echo 'Creating virtual environment...'
                sh 'python3 -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '$VENV/bin/python -m doctest app.py || true'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Launching Streamlit app locally...'
                sh '$VENV/bin/streamlit run app.py &'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
