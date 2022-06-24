pipeline{

    agent {label 'Jenkins-slave'}

	environment {
		DOCKERHUB_CREDENTIALS=credentials('jenkins-dockerhub')
	}

	stages {
	    
	    stage('gitclone') {

			steps {
				git 'https://github.com/software12varal/chat-app.git'
			}
		}

		stage('Build') {

			steps {
				sh 'sudo docker build -t keerthanakumar12/chatapp:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'sudo docker push keerthanakumar12/chatapp:latest'
			}
		}
	}

	post {
		always {
			sh 'sudo docker logout'
		}
	}

}