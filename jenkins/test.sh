#!bin/bash

echo "Test stage"

#venv created, sourced 
python3 -m venv venv
source venv/bin/activate

# pip3 installs, pytest, flask_testing, frontend requirements.txt and backend requirements.txt
pip3 install pytest flask_testing
pip3 install -r frontend/requirements.txt 
pip3 install -r backend/requirements.txt
 
# run pytest frontend 
python3 -m pytest frontend

# run pytest backend
python3 -m pytest backend

deactivate
rm -rf venv

