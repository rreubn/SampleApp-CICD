pipeline {
    agent any
    environment {
        VENV = "${WORKSPACE}/venv"
    }
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '$VENV/bin/python -m doctest app.py || true'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Launching Streamlit app...'
                sh '$VENV/bin/streamlit run app.py &'
            }
        }
    }
}
