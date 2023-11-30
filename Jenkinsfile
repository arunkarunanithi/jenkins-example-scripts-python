pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('EC2 Instance') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
