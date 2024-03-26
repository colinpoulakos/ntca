pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'python3 helloworld.py'
            }
        }
        stage('List') {
            steps {
                sh 'ls'
            }
        }
        stage('Read') {
            steps {
                sh 'python3 readcfg.py > output.txt'
                sh 'cat output.txt'
            }
        }
        stage('Echo and Push to Git') {
            steps {
                script {
                    sh 'cat output.txt'
                    
                    // Initialize a Git repository
                    sh 'git init'
                    
                    // Add the file to the Git index
                    sh 'git add output.txt'
                    
                    // Commit the changes
                    sh 'git commit -m "Add output.txt"'
                    
                    // Push the changes to a remote repository
                    sh 'git remote add origin https://github.com/colinpoulakos/ntca'
                    sh 'git push -u origin main' // You may need to adjust the branch name
                }
            }
        }
    }
}
