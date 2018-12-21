pipeline
{
    parameters
    {
        string(name: 'REPOSITORY_URL', defaultValue: '', description: '<BR><font color=RED>*</font> URL to GIT repository')
        string(name: 'GIT_REPO_CRED', defaultValue: '', description: '<BR><font color=RED>*</font> Credential name of GIT user')
        string(name: 'BRANCH', defaultValue: 'master', description: '<BR>Name of branch (default: master)')
        string(name: 'REQUIREMENTS_FILE', description: '<BR>Relative path to the requirements file')
        string(name: 'PYTHON_SCRIPT_FILE', description: '<BR><font color=RED>*</font> Relative path to the python script')
        text(name: 'GROOVY_SCRIPT', defaultValue: '', description: '<BR>Insert a groovy script text to run.<BR>e.g.:<br>env.PARAM1=&quot;value1&quot;<br>env.PARAM2=&quot;value2&quot;')
    }

    options
    {
        buildDiscarder(logRotator(numToKeepStr: '100', daysToKeepStr: '45'))
        timestamps()
    }

    agent
    {
        kubernetes {
      //cloud 'kubernetes'
      label 'mypod'
      containerTemplate {
        name 'python'
        image 'python'
        ttyEnabled true
        command 'cat'
      }
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
                    sh "ls -la /var/run/docker.sock"
                    sh "python ./${PYTHON_SCRIPT_FILE}"
                }
            }
        }
    }
}
