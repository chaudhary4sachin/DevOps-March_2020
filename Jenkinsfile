pipeline {
  agent { docker { image 'python:2.7.16' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test_calculator.py'
      }   
    }
  }
}
