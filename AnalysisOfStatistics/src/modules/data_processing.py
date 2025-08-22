import pandas as pd

def load_and_explore_data(data_path='../data/pantano_data.csv'):
    ''' Para cargar y mostrar información de the Baells dataframe
    Args: data_path (str): ruta donde se encuentra la CSV file
    Regresa: el DF cargado '''
    #cargar el dataset
    df = pd.read_csv(data_path)
    #5 primeras filas
    print('Primeras 5 filas del dataset (Baells):')
    print(df.head())
    #mostrar las columnas
    print('\nColumnas del dataset:')
    print(list(df.columns))
    #mostrar la información del dataset
    print('\nInformación del dataset:')
    df.info()

    return df
