@echo off

REM Check if installation flag exists
if exist installation.flag (
    echo Installation flag found. Skipping installation.
    goto :run_script
)

REM Define Python version and installer URL
set PYTHON_VERSION=3.12.4
set PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    REM Python is not installed, so download and install it
    echo Installing Python...
    bitsadmin.exe /transfer pythonInstaller /download /priority normal %PYTHON_INSTALLER_URL% python-installer.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python installation complete.
) else (
    echo Python is already installed.
)

REM Install required Python packages
echo Installing required Python packages...
python -m pip install pywin32
echo Required Python packages installation complete.

REM Create a flag file to indicate installation completion
echo Installation completed > installation.flag

:run_script
REM Run the Python script
echo Running Python script...
python resize_habbo.py
