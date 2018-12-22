
# Start from official base image
FROM jenkins/jenkins:2.90

USER root

# Install maven
RUN apt-get update -y && apt-get install maven -y && rm -rf /var/lib/apt/lists/*

USER jenkins

# Copy plugin list
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

# Workaround plugin download issues
ENV CURL_CONNECTION_TIMEOUT=60 JENKINS_UC_DOWNLOAD="http://mirrors.jenkins-ci.org"

# Install plugins
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Setup credentials
ENV JENKINS_USER=admin JENKINS_PASS=admin

# Skip wizard, setup verbose logging
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false"

# Copy seed job and pipelines definition
#ADD jobs.groovy Jenkinsfile-call-junit-generator.groovy Jenkinsfile-junit-generator.groovy /tmp/

# Copy init script
#COPY 10-init.groovy /usr/share/jenkins/ref/init.groovy.d/
