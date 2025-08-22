"""Module para preprocessing y analyzing the Baells para ejercicio 2."""

import pandas as pd
from datetime import datetime as dt
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  #Force TkAgg backend, en VS esto es escencial sino no funciona
import os
from scipy.signal import savgol_filter

def preprocess_data(df):
    '''Aqui se procesa, limpia y filtra el DataFrame
    Args:
        df (pandas.DataFrame): DataFrame de entrada con los datos del pantano.
    Regresa:
        pandas.DataFrame: DataFrame filtrado solo con datos de la Baells, con columnas renombradas y limpias.
    '''
    
    print(f'Imprime el número de filas: {len(df)}')

    dicc={'Dia':'dia','Estació':'estacio','Nivell absolut (msnm)':'nivell_msnm','Percentatge volum embassat (%)':'nivell_perc','Volum embassat (hm3)':'volum'}
    df_baells = df.rename(columns=dicc)
    #x.split() divide el texto en una lista de palabras
    #[2:] elimina las dos primeras palabras
    #' '.join(...) vuelve a unir las palabras restantes en un solo string.
    df_baells['estacio']=df_baells['estacio'].apply(lambda x: ' '.join(x.split()[2:]) if isinstance(x, str) else x)
    df_baells['estacio'] = df_baells['estacio'].str.replace(r'\([^)]*\)', '', regex=True).str.strip()
    df_filtrado=df_baells[df_baells['estacio']=='la Baells']
    #verificar los cambios
    print(f'Data frame limpiado: \n{df_baells.head()}')
    print(f'Data Frame filtrado (solo la Baells): \n{df_filtrado.head()}')

    return df_filtrado

def toYearFraction(date):
    '''Aqui se convierte dia a decimal year
    Args:
        date(datetime.datetime)
    Regresa:
        float: en año en decimal'''
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

def convert_dates(df_filtrado):
    '''Aqui se convierte la columna día del DF a tipo datetime y se genera una columna extra del decimal del año
    Args:
        df_filtrado
    Regresa:
        DF con la nueva columna 'dia_ decimal' '''
    df_filtrado['dia']=pd.to_datetime(df_filtrado['dia'])
    df_subset = df_filtrado[['dia']].head()
    print(f'Data Frame columna dia a datetime: \n{df_subset}')
    tipo_columna_dia = df_filtrado['dia'].dtype
    print(f'Tipo de datos de la columna dia: {tipo_columna_dia}')
    #ordenar de forma ascendente
    df_filtrado = df_filtrado.sort_values(by='dia', ascending=True)
    fecha_antigua=df_filtrado['dia'].iloc[0]
    fecha_reciente=df_filtrado['dia'].iloc[-1]
    df_subset2 = df_filtrado[['dia']].head()
    print(f'Data Frame ordenado por fehca: \n{df_subset2}')
    print(f'\nLa fecha más antigua es: {fecha_antigua}')
    print(f'\nLa fecha más receinte es: {fecha_reciente}')
    print(f'\nTenemos un total de: {len(df_filtrado)} filas')
    df_filtrado['dia_decimal']=df_filtrado['dia'].apply(toYearFraction)
    print(f'\nData Frame ordenado por fecha: \n{df_filtrado.head()}')

    #para que pueda guardarse la imagen en la ruta relativa img
    img_dir = os.path.join(os.path.dirname(__file__), '..', 'img')
    os.makedirs(img_dir, exist_ok=True)

    plt.plot(df_filtrado['dia'], df_filtrado['nivell_perc'])
    plt.xlabel('Tiempo')
    plt.ylabel('Volumen (%)')
    plt.suptitle('Mariel Nava Rodríguez')

    #guarda the plot a img/labells_mariel.png
    output_path = os.path.join(img_dir, 'labells_mariel.png')
    plt.savefig(output_path)
    print(f"Plot saved as {output_path}")
    plt.show()
    return df_filtrado
def smooth_data(df_filtrado):
    '''
    Qui se hace el Smooth de la columna 'nivell_perc' usando Savitzky-Golay 
    Args: 
        df_filtrado
    Regresa:
        el DF con la nueva columna nivell_perc_smoothed
    '''
    #aplicar el filtro Savitzky-Golay 
    window_length = 1500
    polyorder = 3
    if len(df_filtrado) < window_length:
        raise ValueError(f'DataFrame tiene {len(df_filtrado)} filas , pero tu tamaño de la ventana es:  {window_length}. Tendrás que reducirlo.')
    df_filtrado['nivell_perc_smoothed'] = savgol_filter(df_filtrado['nivell_perc'], window_length=window_length, polyorder=polyorder)
    
    img_dir = os.path.join(os.path.dirname(__file__), '..', 'img')
    os.makedirs(img_dir, exist_ok=True)

    #plot original and smoothed data
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtrado['dia_decimal'], df_filtrado['nivell_perc'], label='Original', alpha=0.5)
    plt.plot(df_filtrado['dia_decimal'], df_filtrado['nivell_perc_smoothed'], label='Smoothed', linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Volume (%)')
    plt.title('Baells Reservoir Volume (Original vs Smoothed)')
    plt.suptitle('Mariel Nava Rodríguez')
    plt.legend()
    
    #Guardar el pot
    output_path = os.path.join(img_dir, 'labaells_smoothed_mariel.png')
    plt.savefig(output_path)
    print(f"Smoothed plot saved as {output_path}")
    plt.show()

    return df_filtrado

def calcula_periodos(df_filtrado):
    '''Regresar una lista de periodos en donde:
    Periodo: empieza cuando el valor baja de 60% y termina cuando sube del 60%
    Args: 
        df_filtrado
    Regresa:
        la lista de los periodos de sequia '''
    periods=[]
    limite=60
    bajando=False
    for i in range (len(df_filtrado)):
        if  df_filtrado['nivell_perc_smoothed'].iloc[i]<limite and not bajando:
           valor1=df_filtrado['dia_decimal'].iloc[i]
           bajando=True
        if bajando==True and df_filtrado['nivell_perc_smoothed'].iloc[i]>=limite:
            valor2=df_filtrado['dia_decimal'].iloc[i-1]
            periods.append([round(valor1, 2), round(valor2, 2)])
            bajando = False
        elif i == len(df_filtrado) - 1 and bajando:
            valor2 = df_filtrado['dia_decimal'].iloc[i]
            periods.append([round(valor1, 2), round(valor2, 2)])
    print("La lista de periodos es:")
    for period in periods:
        print(f"[{period[0]}, {period[1]}]")
    return periods

