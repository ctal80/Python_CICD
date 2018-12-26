#!/bin/bash

# Setup
docker build --no-cache -t ctal80:jenkinsmaster .
docker run -d -p 8080:8080 -p 50000:50000 --name jenkinsmaster ctal80:jenkinsmaster
