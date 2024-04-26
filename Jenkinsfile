pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                // Install dependencies if needed
                sh 'pip install selenium'
                sh 'pip install allure-pytest'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run the test script
                sh 'pytest test_script.py --alluredir allure-results'
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                // Generate Allure report
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']],
                    reportBuildPolicy: 'ALWAYS',
                    report: 'allure-report'
                ])
            }
        }
    }
}
