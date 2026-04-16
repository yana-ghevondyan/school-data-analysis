import numpy as np

def mean_array(arr):
    return np.mean(arr)

def min_max(arr):
    return np.min(arr), np.max(arr)

def get_column(df, column_name):
    return df[column_name]
