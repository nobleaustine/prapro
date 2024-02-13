from task_4 import df,file_path
import pandas as pd
from pathlib import Path

def test_dataframe():
    assert isinstance(df,pd.DataFrame) == True

def test_path():
    assert Path(file_path).is_file() and file_path.endswith('.parquet')

