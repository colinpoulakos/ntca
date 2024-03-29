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
        stage('Ansible Lint') {
            steps {
                sh 'ansible-lint --version'
            }
        }
    }
}
