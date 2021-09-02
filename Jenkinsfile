pipeline {
    agent none
    stages {
        stage ('clone ropository') {
            agent {
                label 'master'
            }
            steps {
                git url: 'https://github.com/Bird1993/webapp.git'
            }
        }
        stage ('build conteiner') {
            agent {
<<<<<<< HEAD
                dockerfile {
                    filename 'Dockerfile'
                    dir '.'
                    label 'front_1'
=======
                label 'master'
>>>>>>> f77edf69937e66a24bbdb97a64848e6dc106bcce
                }
            steps {
                sh 'docker build -t public.ecr.aws/b6i1x3c2/webapp:${BUILD_NUMBER} .'
            }            
        }
    }
}
