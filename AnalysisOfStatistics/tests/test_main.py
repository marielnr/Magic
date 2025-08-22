import os
import pytest
from unittest.mock import patch
import importlib
import sys
import pandas as pd

dates = pd.date_range(start='2023-01-01', periods=1500, freq='D').strftime('%Y-%m-%d').tolist()
mock_df = {
    'Dia': dates,
    'Estació': ['Estació Estació la Baells'] * 1500,  #igualar preprocess_data's split()[2:] logic
    'Nivell absolut (msnm)': list(range(1000, 2500)),
    'Percentatge volum embassat (%)': list(range(50, 1550)),
    'Volum embassat (hm3)': list(range(100, 1600))
}

#Fixture= para importar main con el path ajustado
@pytest.fixture
def setup_main():
    import sys
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
    print(f"Debug: Adding to sys.path: {src_path}")  #verificar el path
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    else:
        print(f"Debug: {src_path} already in sys.path")
    
    main_module = importlib.import_module('src.main')
    yield main_module
    #un cleanup 
    if src_path in sys.path:
        sys.path.remove(src_path)

#simular argumentos
@pytest.mark.parametrize("args, expected_ex, should_exit", [
    (["main.py"], 5, False),  #default -ex 5, no exit (runs all exercises)
    (["main.py", "-ex", "1"], 1, False),  #exercise 1, no exit
    (["main.py", "-ex", "3"], 3, False),  #exercise 3, no exit
])
def test_main_parse_args(monkeypatch, setup_main, args, expected_ex, should_exit):
    """
    Test main.py argument parsing and exercise execution.
    """
    main = setup_main  #imported main module
    monkeypatch.setattr(sys, 'argv', args)
    with patch('pandas.read_csv') as mock_read_csv:
        
        mock_read_csv.return_value = pd.DataFrame(mock_df)
        main.main()  # correr el programa sin esperar SystemExit para todos los casos