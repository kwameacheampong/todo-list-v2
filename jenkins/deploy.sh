#!bin/bash

echo "Deploy stage"


ssh jenkins@develop-server-jenkins docker stack deploy --compose-file docker-compose.yaml todo-app
