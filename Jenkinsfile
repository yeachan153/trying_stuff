def gv

pipeline {

    agent any

    stages {
        
        stage('init') {
            steps {
                script {
                    gv = load "script.groovy"
                }
            }
        }
        stage('build') {
            steps {
                script {
                    gv.buildApp()
                }
            }
        }
        stage('test') {
            steps {
                script {
                    gv.testApp()
                }
            }
        }
        stage('deploying') {
            steps {
                script {
                    gv.deployApp()
                }
            }
        }

    }

}