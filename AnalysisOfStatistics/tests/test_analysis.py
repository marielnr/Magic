import pandas as pd
from datetime import datetime
from unittest.mock import patch
import pytest
from src.modules.analysis import preprocess_data, toYearFraction, convert_dates, smooth_data, calcula_periodos

def test_preprocess_data():
    """
    Pruebas de preprocess_data para asegurar el filtrado de 'la Baells' .
    """

    data = {
        'Dia': ['2023-01-01', '2023-01-02'],
        'Estació': ['Estació Estació la Baells', 'Estació Estació otra estación'],  #split()[2:] gives 'la Baells'
        'Nivell absolut (msnm)': [1000, 1001],
        'Percentatge volum embassat (%)': [50, 60],
        'Volum embassat (hm3)': [100, 101]
    }
    df = pd.DataFrame(data)
    result = preprocess_data(df)
    assert not result.empty, "DataFrame no debería estar vacía"
    assert (result['estacio'] == 'la Baells').all(), "Todas las filas deberán ener 'estacio' as 'la Baells'"
    assert 'dia' in result.columns, "Columna 'dia' debería estar presente"
    assert 'nivell_msnm' in result.columns, "Columna 'nivell_msnm' debería estar presente"
    assert 'nivell_perc' in result.columns, "Columna 'nivell_perc' debería estar presente"
    assert 'volum' in result.columns, "Columna 'volum' debería estar presente"

def test_preprocess_data_empty():
    """
    Preuba de preprocess_data pero con un dataframe vacío.
    """
    df = pd.DataFrame()
    with pytest.raises(KeyError, match='estacio'):
        preprocess_data(df)

def test_toYearFraction():
    """
    Prueba de toYearFraction para asegurar que convierte un datetime a decimal year correctamente.
    """
    date = datetime(2023, 6, 15)
    result = toYearFraction(date)
    assert isinstance(result, float), "El resultado debería de ser float"
    assert 2023.0 < result < 2024.0, "El resultado debería de estar entre 2023 y 2024"
    date_edge = datetime(2023, 1, 1)
    result_edge = toYearFraction(date_edge)
    assert result_edge == 2023.0, "Enero 1st debe regresar el año exacto"

def test_convert_dates():
    """
    Prueba de convert_dates para asegurar que conviertet 'dia_decimal' y 'dia' to datetime.
    """
    data = {
        'dia': ['2023-01-01', '2023-01-02'],
        'estacio': ['la Baells', 'la Baells'],
        'nivell_perc': [50, 60]
    }
    df = pd.DataFrame(data)
    with patch('matplotlib.pyplot.show'):
        with patch('matplotlib.pyplot.savefig'):
            result = convert_dates(df)
    assert 'dia_decimal' in result.columns, "Columna 'dia_decimal' debería estar presente"
    assert pd.api.types.is_datetime64_any_dtype(result['dia']), "Columna 'dia' debería ser datetime"
    assert all(result['dia_decimal'].apply(lambda x: isinstance(x, float))), "Todos los valores 'dia_decimal' debern ser floats"

def test_smooth_data():
    """
    Prueba smooth_data para asegurar que añade una columna smoothed column al DataFrame.
    """
    # Use 1500 rows to satisfy window_length=1500
    data = {
        'dia_decimal': [i / 1500 for i in range(1500)],
        'nivell_perc': [50 + (i % 100) / 100 for i in range(1500)]
    }
    df = pd.DataFrame(data)
    with patch('matplotlib.pyplot.show'):
        with patch('matplotlib.pyplot.savefig'):
            result = smooth_data(df)
    assert 'nivell_perc_smoothed' in result.columns, "Columna 'nivell_perc_smoothed' debería estar presente"
    assert len(result['nivell_perc_smoothed']) == len(df), "Smoothed column debería tener el mimso tamaño que el input"
    assert all(result['nivell_perc_smoothed'].notna()), "Smoothed values no deberían de ser NaN"

def test_calcula_periodos():
    """
    Prueba calcula_periodos para identificar los periodos de sequía (debajo del 60%)
    """
    data = {
        'dia_decimal': [2000.0, 2000.1, 2000.2, 2000.3, 2000.4],
        'nivell_perc_smoothed': [70, 55, 50, 58, 65]
    }
    df = pd.DataFrame(data)
    periods = calcula_periodos(df)
    assert len(periods) == 1, "Debería de detectar un periodo"
    assert periods[0][0] == 2000.1, "EL periodo deberia de empezar en 2000.1"
    assert periods[0][1] == 2000.3, "EL periodo deberia de terminar en 2000.3"
    data_empty = {'dia_decimal': [2000.0, 2000.1], 'nivell_perc_smoothed': [70, 75]}
    df_empty = pd.DataFrame(data_empty)
    assert calcula_periodos(df_empty) == [], "Ningún periodo debería ser erronamente detectado (arriba del 60%)"