FROM python:3

# install some generic Python modules
RUN pip install ansible
RUN pip install boto
RUN pip install credstash
RUN pip install fasteners
RUN pip install futures
RUN pip install PyYAML
RUN pip install hvac
RUN pip install awscli
RUN pip install docker

# install docker client
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu trusty stable" && \
    apt-get update && \
    apt-get install -y docker-ce
