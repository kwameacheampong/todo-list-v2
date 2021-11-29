#!bin/bash

echo "Deploy stage"


ssh jenkins@development-server-jenkins docker stack deploy --compose-file docker-compose.yaml todo-app
