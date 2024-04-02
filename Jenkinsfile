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
                sh 'python3 readcfg.py >> output.txt'
                sh 'cat output.txt'
            }
        }
        stage('Ansible Lint') {
            steps {
                sh 'ansible-galaxy collection install arista.eos'
                sh 'ansible-lint bgp.yml >> lintout.txt'
                sh 'cat lintout.txt'
            }
        }
        stage('Ansible Lintout') {
            steps {
                sh 'cat lintout.txt'
            }
        }
    }
}
