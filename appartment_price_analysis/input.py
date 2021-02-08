# -*- coding: utf-8 -*-
# @Author : LE Yao
# @File : input.py

import pandas as pd

data_xls = pd.read_excel('district_info.xlsx', index_col=0)
data_xls.to_csv('district_info.csv', encoding='utf-8')

district_lst = []
with open("district_info.csv", encoding="utf-8") as file:
    file.readline()
    for line in file:
        lst = []
        row = line.strip().split(",")
        for district in row:
            if district != "":
                lst.append(district)
        district_lst.append(lst)

# a dictionary that transform direction in Chinese to English
direction_lst = {"西南": "Southwest", "西北": "Northwest", "东北": "Northeast", "东南": "Southeast",
                 "东": "East", "南": "South", "西": "West", "北": "North"}

dict_district = {1: "LongGang", 2: "NanShan", 3: "GuangMing", 4: "BaoAn", 5: "LongHua",
                 6: "FuTian", 7: "LuoHu", 8: "YanTian", 9: "PingShan", 10: "DaPeng"}

dict_direction = {1: "Southwest", 2: "Northwest", 3: "Northeast", 4: "Southeast",
                  5: "East", 6: "South", 7: "West", 8: "North"}

# a helper method
def district_trans(name):
    for i in range(len(district_lst)):
        if name in district_lst[i]:
            return district_lst[i][0]


# a helper method
def direction_trans(dire):
    return direction_lst[dire]


# some input helper methods
def district_input():
    num = input("Please enter the number of district you want to search for: \n"
                 "LongGang -> 1\n"
                 "NanShan -> 2\n"
                 "GuangMing -> 3\n"
                 "BaoAn -> 4\n"
                 "LongHua -> 5\n"
                 "FuTian -> 6\n"
                 "LuoHu -> 7\n"
                 "YanTian -> 8\n"
                 "PingShan -> 9\n"
                 "DaPeng -> 10\n"
                 "input: ").strip()
    try:
        num = int(num)
        return dict_district[num]
    except:
        print("district: invalid input!")
        return "invalid input"

def direction_input():
    num = input("Please enter the number of direction: \n"
                "Southwest -> 1\n"
                "Northwest -> 2\n"
                "Northeast -> 3\n"
                "Southeast -> 4\n"
                "East -> 5\n"
                "South -> 6\n"
                "West -> 7\n"
                "North -> 8\n"
                "input: "
                ).strip()
    try:
        num = int(num)
        return dict_direction[num]
    except:
        print("direction: invalid input!")
        return "invalid input"


def metro_input():
    flag = input("Please enter 1 if you want a apartment near a metro station.\n"
                 "Otherwise please enter 0.\n"
                 "input: ").strip()
    try:
        res = int(flag)
        return res
    except:
        print("nearMetro: invalid input!")


def layout_input():
    num_bedroom = input("Number of bedrooms: \n").strip()
    num_living = input("Number of living rooms: \n").strip()
    try:
        n1 = int(num_bedroom)
        n2 = int(num_living)
        layout = "{}B{}L".format(n1, n2)
        return layout
    except:
        print("layout: invalid input.\nPlease enter a number!")
        return "invalid input"

