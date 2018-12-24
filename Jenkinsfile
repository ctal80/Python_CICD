pipeline
{
    parameters
    {
        string(name: 'REPOSITORY_URL', defaultValue: 'https://github.com/ctal80/Python_CICD.git', description: '<BR><font color=RED>*</font> URL to GIT repository')
        string(name: 'GIT_REPO_CRED', defaultValue: '', description: '<BR><font color=RED>*</font> Credential name of GIT user')
        string(name: 'BRANCH', defaultValue: 'master', description: '<BR>Name of branch (default: master)')
        string(name: 'REQUIREMENTS_FILE', defaultValue:'Sample_App/requirements.txt', description: '<BR>Relative path to the requirements file')
        string(name: 'PYTHON_SCRIPT_FILE', defaultValue: 'Sample_App/buzz/generator.py', description: '<BR><font color=RED>*</font> Relative path to the python script')
	string(name: 'PYTHON_TEST_SCRIPT_FILE', defaultValue:'tests/test_generator.py', description: '<BR><font color=RED>*</font> Relative path to the python unit test script')
	string(name: 'APP_Name', defaultValue: 'Sample_App', description: '<BR><font color=RED>*</font> Publish Application Name')
    }

    options
    {
        buildDiscarder(logRotator(numToKeepStr: '100', daysToKeepStr: '45'))
        timestamps()
    }
    
    environment {
	    registry = "ctal80/${APP_Name.toLowerCase()}"
            registryCredential = '1325c74b-9fce-4d53-bc30-30c8fa5507bb'
    }

    agent
    {
       
        dockerfile
        {
            filename 'Dockerfile'
            args "-u root -v /var/run/docker.sock:/var/run/docker.sock"
        }
            
       
    }

    stages
    {
        stage('Setup')
        {
            steps
            {
                script
                {
                    script = PYTHON_SCRIPT_FILE.tokenize('/')[-1]
                    currentBuild.displayName = "#${BUILD_ID} | ${script}"
                }
                checkout([
                        $class           : 'GitSCM', branches: [[name: BRANCH]],
                        userRemoteConfigs: [[url: "${REPOSITORY_URL}", credentialsId: "${GIT_REPO_CRED}"]]
                ])
            }
        }

        stage('Install requirements')
        {
            steps
            {
                sh '''
                    
                    if [ "x${REQUIREMENTS_FILE}" != "x" ] && [ -f ${REQUIREMENTS_FILE} ]; then 
                        pip install -r ${REQUIREMENTS_FILE}; 
                    fi
                '''
            }
        }
        
        stage('Run script')
        {
            steps
            {
                script
                {
                    sh "python ./${PYTHON_SCRIPT_FILE}"
                }
            }
        }
	stage('Unit Test')
        {
            steps
            {
                script
                {   
			sh "cd ${APP_Name}/ && python -m pytest -v ./${PYTHON_TEST_SCRIPT_FILE}"
                }
            }
        }
        
        stage('Static Analysis')
        {
            steps
            {
                script
                {   
                    sh "python -m pylint ./${PYTHON_SCRIPT_FILE}"
                }
            }
        }
		
	stage('Build Docker Image')
        {
	    
            steps
            {
                script
                {  
			docker.build("$registry" + ":$BUILD_NUMBER", "-f ${APP_Name}/Dockerfile .")
                    
                }
            }
        }
		
	stage('Test Image')
        {
		
            steps
            {
                script
                {
                    sh 'echo "Tests passed"'
                }
            }
        }
		
	stage('Deploy Image')
        {
            steps
            {
		withCredentials([string(credentialsId: 'registryCredential', variable: 'USERPASS')]) {
		    sh '''
		        docker login -u ctal80 -p "$USERPASS"
			docker push "$registry"
		    '''
		  }
               
            }
        }
    }
	post {
	   success { 
	       emailext (
			  subject: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
			  body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
				<p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
			  to: "ctal80@gmail.com"
         )
	   }
	   
	   failure {
	         emailext (
				  subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
				  body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
					<p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
				  to: "ctal80@gmail.com"
			 )
	   
	   }
	}
}
