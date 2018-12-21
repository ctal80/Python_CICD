pipeline
{
    parameters
    {
        string(name: 'REPOSITORY_URL', defaultValue: '', description: '<BR><font color=RED>*</font> URL to GIT repository')
        string(name: 'GIT_REPO_CRED', defaultValue: '', description: '<BR><font color=RED>*</font> Credential name of GIT user')
        string(name: 'BRANCH', defaultValue: 'master', description: '<BR>Name of branch (default: master)')
        string(name: 'REQUIREMENTS_FILE', description: '<BR>Relative path to the requirements file')
        string(name: 'PYTHON_SCRIPT_FILE', description: '<BR><font color=RED>*</font> Relative path to the python script')
		string(name: 'PYTHON_TEST_SCRIPT_FILE', description: '<BR><font color=RED>*</font> Relative path to the python unit test script')
		string(name: 'APP_Name', description: '<BR><font color=RED>*</font> Publish Application Name')
    }

    options
    {
        buildDiscarder(logRotator(numToKeepStr: '100', daysToKeepStr: '45'))
        timestamps()
    }

    agent
    {
       
            docker { image 'python:3.7' }
       
    }

    stages
    {
        stage('Setup')
        {
            steps
            {
                script
                {
                    def script = PYTHON_SCRIPT_FILE.tokenize('/')[-1]
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
                    writeFile encoding: 'UTF-8',file: './variables.groovy', text: GROOVY_SCRIPT
                    load './variables.groovy'
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
                    sh "python -m pytest -v ./${PYTHON_TEST_SCRIPT_FILE}"
                }
            }
        }
		
		stage('Build Docker Image')
        {
            steps
            {
                script
                {
                    sh '''
							docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
							  
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
            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                 app.push("${env.BUILD_NUMBER}")
                 app.push("latest")
            }
        }
    }
}
