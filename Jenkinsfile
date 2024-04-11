pipeline {
    agent any

    stages {
        stage('Ansible Lint') {
            steps {
                sh 'ansible-lint bgp2.yml'
            }
        }
    }
}
