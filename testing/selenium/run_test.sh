#!/bin/bash -x

sudo apt-get install python3-venv 

echo "${SENSOR_IP}"

### STARTING VIRTUAL ENV
python3 -m venv env
source env/bin/activate

### INSTALLING DEP
pip3 install -r requirements.txt

#python -m pytest test.py --alluredir=allure-results
#python -m pytest test.py --junitxml=test-results
python -m pytest test.py --junitxml=test-results.xml -o junit_suite_name=GhostSeleniumTesting
#python -m pytest regrade.py --junitxml=test-results.xml -o junit_suite_name=ReGrade


### DEACTIVATING VIRTUAL ENV
deactivate
