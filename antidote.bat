@echo off
echo Removing the registry entry for startup...

REM Remove the registry entry added for the startup
REG DELETE "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /V "MyApp" /F

echo Registry entry removed. The script will no longer run on startup.

REM Exit the batch script
exit
