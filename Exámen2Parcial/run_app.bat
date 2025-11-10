@echo off
echo ========================================
echo  Sistema de Prediccion de Diabetes
echo  Evaluacion Segundo Parcial
echo ========================================
echo.

REM Verificar que existe la carpeta model_files
if not exist "model_files" (
    echo ERROR: No se encontro la carpeta 'model_files'
    echo.
    echo Por favor ejecuta el notebook Examen_Diabetes_Prediction.ipynb
    echo hasta la seccion de Parte 2 para generar los archivos del modelo.
    echo.
    pause
    exit /b 1
)

REM Verificar que existen los archivos del modelo
if not exist "model_files\diabetes_model.joblib" (
    echo ERROR: No se encontro el archivo 'diabetes_model.joblib'
    echo Por favor ejecuta el notebook completo primero.
    echo.
    pause
    exit /b 1
)

echo Iniciando aplicacion Flask...
echo.
echo La aplicacion estara disponible en: http://localhost:5000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
echo ========================================
echo.

python app.py

pause
