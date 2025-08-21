#!/bin/bash

# Initialising the repo directory structure using shell commands

# starting with the root directory (parent of scripts dir)
cd ..

# create gitignore file with the .env file
echo .env >> .gitignore

touch LICENSE README.md .env .env.example docker-compose.yml 

# create db project folder and navigate to it
mkdir db && cd db

touch init.sql sample.sql README.md

# create services folder and frontend subfolder and navigate to it
cd .. && mkdir -p services/frontend && cd services/frontend

touch Dockerfile README.md

# create collector service subfolder
cd .. && mkdir collector && cd collector && mkdir tests

touch Dockerfile README.md app.py requirements.txt

# create processor service subfolder
cd .. && mkdir processor && cd processor && mkdir tests

touch Dockerfile README.md app.py requirements.txt

# create analytics service subfolder
cd .. && mkdir analytics && cd analytics && mkdir tests sql

touch Dockerfile README.md app.py requirements.txt

cd ../../scripts

touch simulate_visits.py parse_ua.py