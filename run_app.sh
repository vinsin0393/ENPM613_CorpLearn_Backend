#!/bin/bash

# Define the directory for the virtual environment
VENV_DIR="myenv"

# Check if the virtual environment directory exists, if not, create one
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
    echo "Virtual environment created."
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Running the tests with coverage
echo "Running tests with coverage..."
coverage erase
coverage run --source='corpLearnApp/services/' manage.py test corpLearnApp.test_cases.course-tests corpLearnApp.test_cases.user-tests corpLearnApp.test_cases.document-tests --verbosity=2
TEST_STATUS=$?

# Generating coverage report
coverage report
coverage html

# Check if tests were successful
if [ $TEST_STATUS -eq 0 ]; then
    echo "Tests passed successfully. Starting server..."
    python manage.py runserver
else
    echo "Tests failed. Please fix the issues before starting the server."
    exit 1
fi
