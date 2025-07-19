'''
Análisis de estadísticas del pantano de la Baells.

Este script es el punto de entrada principal para ejecutar los ejercicios de la PEC4
de la asignatura Programación para la Ciencia de Datos (UOC).

Autor: Mariel Nava Rodríguez
Correo: mnavaro@up.edu
Fecha: Junio 2025
-ex 1 para correr ejercicio 1
-h para help
'''
"""Main script to run Baells reservoir analysis exercises."""

import argparse
from modules.data_processing import load_and_explore_data
from modules.analysis import preprocess_data
from modules.analysis import convert_dates
from modules.analysis import smooth_data
from modules.analysis import calcula_periodos

def main():
    """Run the specified exercises based on command-line arguments."""
    #argparse.ArgumentParser: cre un objeto para interpetar argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Baells reservoir data analysis")
    #la línea de abajo define un argumento opcional -ex que puede pasar al ejecutar el script para indicar el ejercicio a ejecutar 
    parser.add_argument(
        "-ex", type=int, choices=[1, 2, 3, 4, 5], default=5,
        help="Exercise to run (1-5, default: 5)"
    )
    #aqui se analiza lo que se escribe en la terminal y se guardan los argumentos en args
    args = parser.parse_args()
    #funciona porque se ejecuatara  hasta el ejercicio que se indique 
    print(f"Running Exercise {args.ex}")

    #ejecuta el Exercise 1
    if args.ex >= 1:
        print("\nExercise 1: Load and explore dataset")
        df = load_and_explore_data()
        print("\nExercise 1 completed")
    #ejecuta el Exercise 2
    if args.ex >=2:
        print("\nExercise 2: Analysis limpieza de datos")
        df_baells = preprocess_data(df)
        print("\nExercise 2 completed")
    #ejecuta el Exercise 3
    if args.ex >= 3:
        print("\nExercise 3: Conversión de columna dia")
        df_baells=convert_dates(df_baells)
        print("\nExercise 3 completed")
    #ejecuta el Exercise 4
    if args.ex >= 4:
        print("\nExercise 4: Suavizar gráfico con scipy")
        df_baells=smooth_data(df_baells)
        print("\nExercise 4 completed")
    #ejecuta el Exercise 5
    if args.ex >= 5:
        print("\nExercise 5: Calcula periodos debajo de 60%")
        lista=calcula_periodos(df_baells)
        print("\nExercise 5 completed")
        

if __name__ == "__main__":
    main()
