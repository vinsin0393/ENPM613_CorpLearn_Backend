@echo off

REM Define the directory for the virtual environment
set VENV_DIR=myenv

REM Check if the virtual environment directory exists, if not, create one
if not exist "%VENV_DIR%" (
    python -m venv %VENV_DIR%
    echo Virtual environment created.
)

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Install dependencies from requirements.txt
pip install -r requirements.txt

REM Apply migrations
python manage.py migrate

REM Running the tests with coverage
echo Running tests with coverage...
coverage erase
coverage run --source=corpLearnApp/services/ manage.py test corpLearnApp.test_cases.course-tests corpLearnApp.test_cases.user-tests corpLearnApp.test_cases.document-tests --verbosity=2
set TEST_STATUS=%ERRORLEVEL%

REM Generating coverage report
coverage report
coverage html

REM Check if tests were successful
if %TEST_STATUS% == 0 (
    echo Tests passed successfully. Starting server...
    python manage.py runserver
) else (
    echo Tests failed. Please fix the issues before starting the server.
    exit /b 1
)
