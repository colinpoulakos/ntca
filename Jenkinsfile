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
                sh 'python3 readcfg.py'
            }
        }
    }
}
