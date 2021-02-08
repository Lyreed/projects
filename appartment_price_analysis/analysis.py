# -*- coding: utf-8 -*-
# @Author : LE Yao
# @File : analysis.py

import pandas as pd
from pyecharts.charts import Pie, Bar
from pyecharts import options as opts
from input import district_trans, direction_trans
from math import isnan

# data processing
items_lst = []
with open("房子.csv", encoding="utf-8") as file:
    file.readline()
    for line in file:
        row = line.strip().split(",")
        try:
            name = row[1].strip()
            district = district_trans(row[2])
            price_sum = int(row[-2])
            price = int(row[-1])
            layout = row[3].split("|")[0].replace("室", "B").replace("厅", "L").strip()
            year = int(row[3].split("|")[-2].replace("年建", "").strip())

            direction_lst = row[3].split("|")[2].strip().split(" ")
            direction = ""
            for i in range(len(direction_lst)):
                d = direction_trans(direction_lst[i])
                direction += d + " "
            direction.strip()

            if "地铁" in row[0]:
                nearMetro = 1
            else:
                nearMetro = 0
            items_lst.append([name, district, layout, year, price, price_sum, direction, nearMetro])
        except:
            continue

# create a data frame
data = pd.DataFrame(items_lst, columns=["name", "district", "layout",
                                        "yearBuilt", "price", "price_sum", "direction", "nearMetro"])

group = data.groupby("district")
group_agg = group["price"].agg(["mean", "count"])

# output: a bar chart that displays average price per square meter of apartment in each district
def avgprice_bar():
    group_sorted = group_agg.sort_values("mean", ascending=False)
    bar = Bar(init_opts=opts.InitOpts(page_title="bar chart"))
    bar.add_xaxis(group_sorted.index.tolist())
    bar.add_yaxis(series_name="average price",
                  yaxis_data=[round(n) for n in group_sorted["mean"].tolist()])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Average Price of Apartments"))
    return bar


# input: name of district
# output: a pie chart of year built analysis of apartments in a given district
def yearbuilt_pie(district):
    try:
        temp = data[data["district"].str.contains(district)]["yearBuilt"].value_counts()
        year = temp.index.tolist()[:10]  # top 10
        count = temp.values.tolist()[:10]
        p = Pie().add("", [list(z) for z in zip(year, count)])
        p.set_global_opts(title_opts=opts.TitleOpts(
            title="Year Built --- {}".format(district)))
        p.set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {d}%"))
        return p
    except:
        return "invalid input"


# input: name of district
# output: a pie chart of layout analysis of apartments in a given district
def layout_pie(district):
    try:
        temp = data[data["district"].str.contains(district)]["layout"].value_counts()
        layout = temp.index.tolist()[:10]  # top 10
        count = temp.values.tolist()[:10]
        p = Pie()
        p.add("", [list(z) for z in zip(layout, count)])
        p.set_global_opts(title_opts=opts.TitleOpts(title="layout - {}".format(district)))
        p.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        return p
    except:
        return "invalid input"


# input: district, near metro station or not, direction, layout
# output: average price of the type of apartment you specified
def priceOfApartment(district, layout, nearMetro, direction):
    print("------------------------------------------")
    temp = data[(data["district"].str.contains(district))
                & (data["layout"] == layout)
                & (data["nearMetro"] == nearMetro)
                & (data["direction"].str.contains(direction))]
    result = temp["price"].mean()

    print("INFORMATION")
    print("District: {} district".format(district))
    print("Layout: {}".format(layout))
    if nearMetro == 1:
        flag = "Yes"
    else:
        flag = "No"
    print("Near a metro station or not: {}".format(flag))
    print("Direction: {}".format(direction))
    print("------------------------------------------")

    if isnan(result):
        print("Sorry, there's no information.")
        print("------------------------------------------")
    else:

        print("The average price is about ¥{} per square meter".format(round(result)))
        print("------------------------------------------")

# priceOfApartment("LongHua", "3B1L", 0, "Southwest")
