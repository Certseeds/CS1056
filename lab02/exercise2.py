#!/usr/bin/env python3
# coding=utf-8
'''
Github: https://github.com/Certseeds/CS1056
Organization: SUSTech
Author: nanoseeds
Date: 2020-09-25 15:00:41
LastEditors: nanoseeds
LastEditTime: 2020-09-25 15:38:00
'''
from typing import Dict
import json


def main() -> None:
    """
    hardcode data to a json file
    """
    jsonfile: Dict = {}
    jsonfile['id'] = "0001"
    jsonfile["type"] = "donut"
    jsonfile["name"] = "Cake"
    jsonfile["ppu"] = 0.55
    jsonfile["Batters"] = {}
    jsonfile["Batters"]["Batter"] = []
    jsonfile["Batters"]["Batter"].append({"id": "1001", "type": "Regular"})
    jsonfile["Batters"]["Batter"].append({"id": "1002", "type": "Chocolate"})
    jsonfile["Batters"]["Batter"].append({"id": "1003", "type": "Blueberry"})
    jsonfile["Batters"]["Batter"].append(
        {"id": "1004", "type": "Devil's Food"})
    with open("file.json", mode="w", encoding="UTF-8") as file:
        file.write(json.dumps(jsonfile))


if __name__ == "__main__":
    main()
