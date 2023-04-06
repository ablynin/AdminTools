@echo off
set PythonPath=Z:\python\Python36-32\Scripts
set ProjectPath=Z:\PycharmProjects\AdminTools
%PythonPath%\pylupdate5 %ProjectPath%\AdminTools.py %ProjectPath%\MainWindow.py %ProjectPath%\options.py -ts %ProjectPath%\source\languages\ru_RU.ts
REM @pause
