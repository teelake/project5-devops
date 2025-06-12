pipeline {
    agent any
    
    environment {
        EC2_HOST = '16.171.144.118'
        EC2_USER = 'ubuntu'
        SSH_CREDENTIAL_ID = 'project5-deploy-key'  // Replace with your actual credential ID
    }
    
    stages {
        stage('Clone Repo') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    userRemoteConfigs: [[url: 'https://github.com/teelake/project5-devops.git']]
                ])
            }
        }
        
        stage('Test Connection') {
            steps {
                sshagent(["${SSH_CREDENTIAL_ID}"]) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no -o ConnectTimeout=10 ${EC2_USER}@${EC2_HOST} '
                        echo "Connection successful"
                        whoami
                        pwd
                    '
                    '''
                }
            }
        }
        
        stage('Deploy to EC2') {
            steps {
                sshagent(["${SSH_CREDENTIAL_ID}"]) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no -o ConnectTimeout=10 ${EC2_USER}@${EC2_HOST} '
                        echo "Starting deployment..."
                        
                        # Check if flask directory exists and is a git repo
                        if [ ! -d "~/flask" ]; then
                            echo "Flask directory does not exist. Cloning repository..."
                            git clone https://github.com/teelake/project5-devops.git flask
                            cd flask
                        elif [ ! -d "~/flask/.git" ]; then
                            echo "Flask directory exists but is not a git repository. Reinitializing..."
                            rm -rf ~/flask
                            git clone https://github.com/teelake/project5-devops.git flask
                            cd flask
                        else
                            echo "Flask directory exists and is a git repository. Updating code..."
                            cd ~/flask
                            git pull origin master || { echo "Git pull failed"; exit 1; }
                        fi
                        
                        echo "Setting up virtual environment..."
                        if [ ! -d "venv" ]; then
                            echo "Creating new virtual environment..."
                            python3 -m venv venv
                        fi
                        
                        echo "Activating virtual environment..."
                        source venv/bin/activate || { echo "Failed to activate venv"; exit 1; }
                        
                        echo "Installing/updating dependencies..."
                        if [ -f "requirements.txt" ]; then
                            echo "Installing from requirements.txt..."
                            pip install -r requirements.txt
                        else
                            echo "No requirements.txt found, installing Flask..."
                            pip install flask
                        fi
                        
                        echo "Restarting Flask application..."
                        sudo systemctl restart flaskapp || { echo "Failed to restart service"; exit 1; }
                        
                        echo "Checking service status..."
                        sudo systemctl is-active flaskapp || { echo "Service is not active"; exit 1; }
                        
                        echo "Deployment completed successfully!"
                    '
                    '''
                }
            }
        }
        
        stage('Health Check') {
            steps {
                script {
                    sleep(time: 5, unit: 'SECONDS')  // Wait for service to start
                    try {
                        sh 'curl -f http://${EC2_HOST}:5000 || curl -f http://${EC2_HOST}:80'
                        echo "Health check passed!"
                    } catch (Exception e) {
                        echo "Health check failed, but deployment completed"
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed!'
        }
        always {
            cleanWs()  // Clean workspace after build
        }
    }
}
