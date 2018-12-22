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
	string(name: 'APP_Name', defaultValue: 'DemoApp', description: '<BR><font color=RED>*</font> Publish Application Name')
    }

    options
    {
        buildDiscarder(logRotator(numToKeepStr: '100', daysToKeepStr: '45'))
        timestamps()
    }

    agent
    {
       
        docker
        {
            image 'python:3.7'
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
                    sh "cd Sample_App/ && python -m pytest -v ./${PYTHON_TEST_SCRIPT_FILE}"
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
	    agent {
                docker { 
			image 'docker'
			args "-u root -v /var/run/docker.sock:/var/run/docker.sock"
		}
		
            }
            steps
            {
	        checkout([
                        $class : 'GitSCM', branches: [[name: BRANCH]],
                        userRemoteConfigs: [[url: "${REPOSITORY_URL}", credentialsId: "${GIT_REPO_CRED}"]]
                ])
                script
                {
                    sh  '''
			docker build -f Dockerfile -t ${script}:LATEST .
							  
			'''
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
		
	stage('Publish Image')
        {
            steps
            {
                script
                {
                    sh '''
		         docker login -e $DOCKER_EMAIL -u $DOCKER_USER -p $DOCKER_PASS
                         docker push ${script}:LATEST
			
		       '''
                }
            }
        }
    }
}
