@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    if exist "%LOCALAPPDATA%\Python\bin\python.exe" (
        "%LOCALAPPDATA%\Python\bin\python.exe" -m venv ".venv"
    ) else (
        py -3 -m venv ".venv"
    )
    if errorlevel 1 (
        echo Could not create the Python environment. Install Python 3.
        pause
        exit /b 1
    )
)

".venv\Scripts\python.exe" -m pip install -r "requirements.txt"
if errorlevel 1 (
    echo Dependency installation failed.
    pause
    exit /b 1
)

if /i "%~1"=="--startup" (
    start "" /min ".venv\Scripts\pythonw.exe" "Hackpad DataLink.py"
    exit /b
)

".venv\Scripts\python.exe" "Hackpad DataLink.py"
pause
