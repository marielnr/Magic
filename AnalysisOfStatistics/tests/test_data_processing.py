import pandas as pd
import os
import pytest
from src.modules.data_processing import load_and_explore_data

def test_load_and_explore_data(capsys):
    """
    Prueba de: load_and_explore_data para asegurarnos de que si carga la csv file y que muestra la información.
    """
    # Create test CSV with all required columns
    test_data = {
        'Dia': ['2023-01-01', '2023-01-02'],
        'Estació': ['la Baells', 'la Baells'],
        'Nivell absolut (msnm)': [1000, 1001],
        'Percentatge volum embassat (%)': [50, 60],
        'Volum embassat (hm3)': [100, 101]
    }
    test_df = pd.DataFrame(test_data)
    test_file = 'test_pantano_data.csv'
    test_df.to_csv(test_file, index=False)

    # Run function
    result = load_and_explore_data(data_path=test_file)
    captured = capsys.readouterr()  # Capture printed output

    # Assertions
    assert not result.empty, "DataFrame no debería estar vacío"
    assert 'Dia' in result.columns, "Column 'Dia' debe estar presente"
    assert 'Estació' in result.columns, "Column 'Estació' debe estar presente"
    assert 'Nivell absolut (msnm)' in result.columns, "Column 'Nivell absolut (msnm)' debe estar presente"
    assert 'Percentatge volum embassat (%)' in result.columns, "Column 'Percentatge volum embassat (%)' debe estar presente"
    assert 'Volum embassat (hm3)' in result.columns, "Column 'Volum embassat (hm3)' debe estar presente"
    assert "Primeras 5 filas del dataset (Baells):" in captured.out, "output"
    assert "Columnas del dataset:" in captured.out, "output"
    assert "Información del dataset:" in captured.out, "output"

    # Clean up
    os.remove(test_file)

def test_load_and_explore_data_empty_file(tmp_path):
    """
    Prueba de load_and_explore_data con una CSV file vacía.
    """
    empty_file = tmp_path / "empty.csv"
    with open(empty_file, 'w') as f:
        f.write('')  # Create a completely empty file
    with pytest.raises(pd.errors.EmptyDataError):
        load_and_explore_data(data_path=str(empty_file))

def test_load_and_explore_data_invalid_path():
    """
    Prueba de load_and_explore_data con un file path invalido.
    """
    with pytest.raises(FileNotFoundError):
        load_and_explore_data(data_path="non_existent.csv")

