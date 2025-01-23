@echo off

:: Remove metadata from some files
echo REMOVE METADATA
exiftool -recurse -all= posts/
exiftool -recurse -all= img/

:: Build website
echo BUILD
quarto render

:: Remove extra code
echo CLEANUP
python .\CLEANUP.py

echo DONE
timeout 20
