pyinstaller -F ide.py
cd C:\Users\ASUS\Desktop
del ide.spec
del /s/q __pycache__\*.*
rd __pycache__
del /s/q build\ide\*.*
rd build\ide
rd build
move C:\Users\ASUS\Desktop\dist\ide.exe   C:\Users\ASUS\Desktop
rd dist