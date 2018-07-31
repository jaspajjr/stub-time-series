import pandas as pd


def time_series() -> pd.DataFrame:
    '''
    Loads the time series csv.
    '''
    df = pd.read_csv('/data/data.csv', parse_dates=[0])
    return df
