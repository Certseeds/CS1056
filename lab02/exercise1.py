#!/usr/bin/env python3
# coding=utf-8
'''
Github: https://github.com/Certseeds/CS1056
Organization: SUSTech
Author: nanoseeds
Date: 2020-09-25 14:09:49
LastEditors: nanoseeds
LastEditTime: 2020-10-23 11:35:13
'''
from typing import List
import pandas as pd
from pandas.core.frame import DataFrame


def main(path: str) -> None:
    """[summary]
     Convert the .csv file to a .xlsx file with 14 sheets 
     (the content of every sheet is the each column data of the .csv file)  
    Args:
        path (str): [files path]
    """
    file_inside: DataFrame = pd.read_csv(path)
    sheets: List[DataFrame] = []
    for index, row in file_inside.iteritems():
        sheets.append(row)
    # for i in sheets:
    #     # print(i)
    #     for index, j in enumerate(i):
    #         # print(index,j)
    #         pass
    with pd.ExcelWriter('output.xlsx') as writer:
        for i in sheets:
            i.to_excel(writer, sheet_name=i.name)


if __name__ == "__main__":
    main('./100_Sales_Records.csv')
