@echo off

REM  ▄▄▄██▀▀▀▄▄▄       ███▄ ▄███▓▓█████   ██████
REM    ▒██  ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒
REM    ░██  ▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄
REM ▓██▄██▓ ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒
REM  ▓███▒   ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒
REM  ▒▓▒▒░   ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░
REM  ▒ ░▒░    ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░
REM  ░ ░ ░    ░   ▒   ░      ░      ░   ░  ░  ░
REM  ░   ░        ░  ░       ░      ░  ░      ░
REM
REM          ▄▄▄█████▓ ██░ ██ ▓█████
REM          ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀
REM          ▒ ▓██░ ▒░▒██▀▀██░▒███
REM          ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄
REM            ▒██▒ ░ ░▓█▒░██▓░▒████▒
REM            ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░
REM              ░     ▒ ░▒░ ░ ░ ░  ░
REM            ░       ░  ░░ ░   ░
REM                    ░  ░  ░   ░  ░
REM
REM  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███
REM ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
REM ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
REM ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄
REM ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
REM  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
REM  ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
REM  ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░     ░░   ░
REM  ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░
REM      

setlocal

color 0D
set "PATH=%SystemRoot%\System32;%PATH%"

:menu
echo ===================================
echo    Cyberpunk2077 Mod Creation Tool
echo ===================================
echo.
echo [1] Replace a video (bk2)
echo [2] Replace an image (png)
echo.

set /p choice="Select an option (1 or 2): "

if "%choice%"=="1" (
    call VideoReplacer.bat
	python ModifyScripts.py %choice%
) else if "%choice%"=="2" (
    call ImageReplacer.bat
	python ModifyScripts.py %choice%
) else (
    cls
    goto menu
)

endlocal
