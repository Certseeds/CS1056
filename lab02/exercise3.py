#!/usr/bin/env python3
# coding=utf-8
'''
Github: https://github.com/Certseeds/CS1056
Organization: SUSTech
Author: nanoseeds
Date: 2020-09-25 15:09:42
LastEditors: nanoseeds
LastEditTime: 2020-09-25 15:37:51
'''
from typing import List
import pandas as pd
from pandas import DataFrame
from tables import file
from datetime import datetime


def main(path: str) -> None:
    """
    Based on the 100_Sales_Records.csv, 
    find out sale records with online sale channels, 
    and sort them by the order date
    """
    file_inside: DataFrame = pd.read_csv(path)
    file_inside = file_inside[~file_inside['Sales Channel'].isin(['Offline'])]
    for index, column in file_inside.iterrows():
        file_inside.loc[index, "Order Date"] = datetime.strptime(
            column["Order Date"], "%m/%d/%Y").date()
    file_inside.sort_values("Order Date", inplace=True)
    with pd.ExcelWriter('output2.xlsx') as writer:
        file_inside.to_excel(writer)


if __name__ == "__main__":
    main('./100_Sales_Records.csv')
