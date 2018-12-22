FROM python:3
# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir -p /opt/services/Sample_App/
COPY . /opt/services/Sample_App/
WORKDIR /opt/services/Sample_App/
EXPOSE 5000
# Python dependencies
RUN pip install -r /opt/services/Sample_App/requirements.txt

CMD [ "python", "/opt/services/Sample_App/app.py" ]
