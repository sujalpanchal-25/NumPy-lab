@echo off
git add .
set /p msg=Commit Message:
git commit -m "%msg%"
git push
pause