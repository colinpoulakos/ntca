pipeline {
    agent any

    stages {
        stage('Ansible Lint') {
            steps {
                sh 'ansible-lint --version'
                sh 'ansible-lint bgp.yml'
            }
        }
    }
}
