# Análisis de Estadísticas del Pantano de la Baells

Este proyecto es parte de la PEC4 de la asignatura *Programación para la Ciencia de Datos* del Grado en Ciencia de Datos Aplicada de la UOC. 
Analiza datos del pantano de la Baells para identificar periodos de sequía.
Autora: Mariel Nava Rodríguez

## Estructura del Proyecto

baells_analysis/
├── src/
├───├── __init__.py
│   ├── main.py              #Desde aqui se ejecutan todos los ejercicios
│   ├── modules/
├───│   ├── __init__.py #para indicar que src y src/modules son paquetes
│   │   ├── data_processing.py #Aqui se encuentran funciones para cargar y explorar datos del df
│   │   ├── analysis.py       #Funciones de preprocesado, conversiones, smoothing, y demostración en gráfica de periodos de sequía 
├── tests/
│   ├── test_data_processing.py 
│   ├── test_analysis.py       
├── doc/                     #Aqui se genera la HTML documentation
├── cov_html/                #Aqui se genera los coverage HTML documentation
├── img/                     #Donde se guardan los Plots del ejercisios 3 y 4
├── screenshots/              
├── data/                    #pantano_data.csv, LICENSE, .pylintrc, README.md                 
├── requirements.txt          
                

## Instalación

1. Clona o descomprime el proyecto.
3. Aseguarar que Python 3.8 esta instalado
2. Instala las dependencias:
   ```cmd
   pip install -r requirements.txt

## Creación del entorno virtual
1. Vuelve a verificar que la terminal esté en el directorio raís del proyecto 
2. Activa el entorno virtual: .\venv\Scripts\activate
3. Instala las dependencias requirements.txt: pip install -r requirements.txt
4. Regresa al directorio raiz: cd ..
5.ejecuta: pdoc -o doc src/modules/data_processing.py src/modules/analysis.py

##Antes de ejecutar el código
Antes de ejecutar el código es importante que ejecutes en tu terminal:
cd C:\Users\marie\proyecto_pantano_baells\src
con base en tu ruta. depedneidno cual sea la ruta en la qie psusite el proyecto el "Users\marie" cambiará.
Una vez en el directorio src/, ejecuta el script con los argumentos deseados:
python main.py -ex 5  # Ejecuta todos los ejercicios (1 al 5)
Si indicas .py -ex 4 se ejecutará 1 al 4 y así progresivamente. Esta por default el 5. 

-h o --help: para pedir ayuda

##Para el ejercicio 3
Es importante tener hacer pip install matplotlib en la terminal.
En mi caso yo estaba ejecutando el script en Python 3.13 por lo que instalé ahí matplotlib:
C:/Users/marie/AppData/Local/Programs/Python/Python313/python.exe -m pip install matplotlib
En Visual Studio a veces no funciona el plt.show() por lo que pus ela opción de que le imagen se guarde en la carpeta donde esta el archivo
Hacer lo mismo en la versión de Python que se este ejecutando

##Para el ejercicio 4 
pip install scipy

##Para pruebas (en estas pruebas se importan funciones de los códigos para ser probados con una csv muy pequeña y ver posibles errores) 
1. Activar el virtual environment: venv\Scripts\activate
2. Asegurarte de tener instalados los requirments. De aún no tenerlos ve a la carpeta de inicio con el comando: cd..
Y después usa el comando: pip install -r requirements.txt 
3. $env:PYTHONPATH = "C:\Users\marie\proyecto_pantano_baells"
pytest tests/
4. Si no funcionan puede que funcione borrar el cache de python:
Remove-Item -Recurse -Force src\__pycache__
Remove-Item -Recurse -Force src\modules\__pycache__
Remove-Item -Recurse -Force tests\__pycache__

##Para pylint
1. verificr que pylint esta instalado: pip show pylint sino instalalo: pip install pylint
2. tener el entorno virtual activo: .\venv\Scripts\activate
3. y estar en la raiz del proyecto: cd C:\Users\marie\proyecto_pantano_baells
4. para ejecutar pylint: pylint src/ tests/ 
5. Generar un archivo de configuración: pylint --generate-rcfile > .pylintrc
6. Cambia la extención a .txt para modificarlo y agregar: 
[MESSAGES CONTROL]
disable=
    missing-module-docstring,
    missing-function-docstring,
    line-too-long,
    trailing-whitespace,
    missing-final-newline,
    trailing-newlines,
    bad-indentation,
    wrong-import-position,
    wrong-import-order,
    import-error,
    invalid-name,
    possibly-used-before-assignment,
    unused-variable,
    unspecified-encoding,
    redefined-outer-name,
    reimported,
    import-outside-toplevel,
    unused-argument,
    use-implicit-booleaness-not-comparison,
    pointless-string-statement
7. Regresalo a extensón .pylintrc asegurandote de guardarlo como UTF-8
8. Vuelve a ejecutar en la terminal: pylint src/ tests/



