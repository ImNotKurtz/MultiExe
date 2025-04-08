@echo off
chcp 65001 >nul
cls

:MENU
:: Simula centralização vertical
for /L %%i in (1,1,5) do echo.

:: Centralização horizontal com espaços
set "SPACES=                          "

echo                █▄─▀█▀─▄█▄─██─▄█▄─▄███─▄─▄─█▄─▄█████▄─▄▄─█▄─▀─▄█▄─▄▄─█
echo                ██─█▄█─███─██─███─██▀███─████─███████─▄█▀██▀─▀███─▄█▀█
echo                ▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀
echo ㅤ
echo          ╔═══════════════════════════════════════════════════════════════════╗
echo          ║                                                                   ║
echo          ║      [1] Start MultiExe       [2] Credits      [3] Exit           ║
echo          ║                                                                   ║
echo          ╚═══════════════════════════════════════════════════════════════════╝
echo.

set /p choice=^> 

if "%choice%"=="1" (
    cls
    echo Running builder.py...
    python builder.py
    pause
    goto MENU
) else if "%choice%"=="2" (
    cls
    echo.
    echo ========================================
    echo      Credits
    echo ========================================
    echo    GitHub: https://github.com/ImNotKurtz
    echo.
    pause >nul  :: Espera por uma tecla sem exibir a mensagem
    cls
    goto MENU
) else if "%choice%"=="3" (
    exit
) else (
    echo Opção inválida. Tente novamente.
    timeout /t 2 >nul
    cls
    goto MENU
)
