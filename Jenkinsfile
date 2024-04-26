pipeline {
    agent any  // Use any available agent

    triggers {
        scm { // Trigger on SCM (Git) changes
            $class: 'GitSCM'
            branches: '*/main' // Trigger on changes to the 'main' branch (adjust as needed)
            doFirstMerge: true
            extensions {
                // Optional: Configure GitHub authentication (if needed)
                // See https://jenkins.io/doc/book/pipeline/ SCM-Triggers.html#git-authentication for details
            }
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', // Checkout the 'main' branch (adjust as needed)
                    url: 'https://github.com/anuskhan636/selenium.git' // Replace with your GitHub repository URL
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt' // Install test dependencies
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Adjust the path to `allure-reports` if needed
                    sh 'pytest -s -v test_login.py --alluredir="./allure-reports"'
                }
            }
        }

        stage('Post-Build Actions') {
            always {
                // Archive test reports or artifacts (optional)
                archiveArtifacts '**/*.xml' // Example: Archive all XML files
            }
        }
    }
}
