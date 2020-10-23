
'''
Github: https://github.com/Certseeds/CS1056 
Organization: SUSTech
Author: nanoseeds
Date: 2020-10-09 14:10:47
LastEditors: nanoseeds
LastEditTime: 2020-10-23 15:28:02
'''
from typing import List
import pandas as pd
from pandas.core.frame import DataFrame
from fancyimpute import IterativeImputer as MICE

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

def main(path: str) -> None:
    """[summary]
    Args:
        path (str): [files path]
    """
    fi: DataFrame = pd.read_csv(path, low_memory=False)
    print(fi.shape)
    fi = fi.dropna(axis="rows")
    print(fi.shape)
    print(fi.sum())


def main2(path: str) -> None:
    """[summary]
    Args:
        path (str): [files path]
    """
    fi: DataFrame = pd.read_csv(path, low_memory=False)
    fi = fi.fillna(0)
    print(fi.shape)
    fi = fi.dropna(axis=1)
    print(fi.shape)


def main3(path: str) -> None:
    """[summary]
    Args:
        path (str): [files path]
    """
    fi: DataFrame = pd.read_csv(path, low_memory=False)
    fi = fi.fillna(method="ffill", axis=0)
    print(fi.shape)
    fi = fi.dropna(axis=1)
    print(fi.shape)


def main4(path: str) -> None:
    """[summary]
    Args:
        path (str): [files path]
    """
    fi: DataFrame = pd.read_csv(path, low_memory=False)
    fi = fi.fillna(method="bfill", axis=0)
    print(fi.shape)
    fi = fi.dropna(axis=1)
    print(fi.shape)


def main5(path: str) -> None:
    """[summary]
    Args:
        path (str): [files path]
    """
    fi: DataFrame = pd.read_csv(path, low_memory=False)
    fi = fi.fillna(fi.mean())
    print(fi.shape)
    fi = fi.dropna(axis=1)
    print(fi.shape)


def main6(path: str) -> None:
    """[summary]
    Args:
        path (str): [files path]
    """
    fi: DataFrame = pd.read_csv(path, low_memory=False)
    fi = pd.DataFrame(MICE().fit_transform(fi))
    print(fi.shape)
    fi = fi.dropna(axis=1)
    print(fi.shape)


if __name__ == "__main__":
    file_path: str = "melb_data.csv"
    main(file_path)
    main2(file_path)
    main3(file_path)
    main4(file_path)
    main5(file_path)
    main6(file_path)
