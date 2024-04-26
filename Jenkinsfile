pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=reports'
            }
        }

        stage('Generate Allure report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports']],
                    reportBuildPolicy: 'ALWAYS',
                    report: 'allure-report'
                ])
            }
        }
    }
}
