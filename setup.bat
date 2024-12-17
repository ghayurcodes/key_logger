@echo off
echo Installing required packages...
REM Install dependencies using requirements.txt
python -m pip install -r requirements.txt

echo Running the main program in the background...
REM Run the main.py script in the background
start /B python main.py

echo Adding the script to startup...

REM Create a registry entry to run the script on startup
REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /V "MyApp" /t REG_SZ /F /D "\"%CD%\main.py\""

echo Setup complete. The script will now run on startup.
REM Exit the batch script after starting the program
exit
