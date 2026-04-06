import pandas as pd
from pandas import DataFrame
from pathlib import Path

def read_csv_file(path: Path, sep: str):
    if path is None or sep is None:
        raise ValueError('Invalid file name or separator')
    
    data_frame = pd.read_csv(path, sep=sep)

    print(f'Всего слов прочитано: {len(data_frame)}')
    print(data_frame.columns.tolist())
    return data_frame

def save_csv_file(data_frame: DataFrame, path_to_save: Path):
    if data_frame is None:
        raise ValueError('Invalid data frame for save to csv file')
    if path_to_save is None:
        raise ValueError('Saving path is empty')
    if not isinstance(path_to_save, Path):
        raise ValueError('Incorrect path type')
    
    path_to_save.parent.mkdir(parents=True, exist_ok=True)
    data_frame.to_csv(path_to_save, index=False)