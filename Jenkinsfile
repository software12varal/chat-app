pipeline {
    
    agent {
        docker {
            image 'python:3.8-slim-buster'
            args '-p 3000:3000 -p 5000:5000' 
        }
    }

    stages {

        stage("build") {
            
            //outlines the steps to be used e.g pip install; simply steps on a command line.
            steps {
                sh """
                    docker build -t chat app .
                """
            }
        }
        
        stage("test") {

            steps {
                sh """
                    docker run --rm chat app
                """
            }
        }
       
        stage("deploy") {

            steps {
                echo 'deploying the application'
            }
        }
        
    }
}