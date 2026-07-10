@echo off
REM ============================================================
REM  Bootcamp-QA - Script de inicializacion
REM  Crea el entorno virtual e instala las dependencias
REM  (selenium, requests, pytest) para ejecutar las suites.
REM ============================================================
cd /d "%~dp0"

REM Detectar el comando de Python real (el alias "python" de la
REM Microsoft Store existe en el PATH pero no ejecuta nada)
set "PYTHON="
py --version >nul 2>nul
if not errorlevel 1 set "PYTHON=py"
if not defined PYTHON (
    python --version >nul 2>nul
    if not errorlevel 1 set "PYTHON=python"
)
if not defined PYTHON (
    echo [ERROR] Python no esta instalado o no esta en el PATH.
    echo Descargalo desde https://www.python.org/downloads/
    pause
    exit /b 1
)

if not exist venv (
    echo Creando entorno virtual...
    %PYTHON% -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo Instalando dependencias...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ============================================================
echo  Listo. Para activar el entorno en una nueva terminal:
echo      venv\Scripts\activate
echo  Ejemplo para correr las pruebas de API:
echo      pytest 03-pruebas-de-api-python
echo ============================================================
pause
