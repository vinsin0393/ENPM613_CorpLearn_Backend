@echo off

REM Define the virtual environment directory
set VENV_DIR=myenv

REM Check if the virtual environment directory exists, if not, create one
if not exist "%VENV_DIR%" (
    python -m venv %VENV_DIR%
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Check if requirements.txt exists
if exist "requirements.txt" (
    REM Install dependencies from requirements.txt
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Please ensure the file exists in the current directory.
    exit /b
)

REM Apply migrations
python manage.py makemigrations
python manage.py migrate

REM Run the Django development server
python manage.py runserver

REM Deactivate virtual environment on exit
call %VENV_DIR%\Scripts\deactivate

echo Script execution completed. Press any key to exit.
pause > nul
