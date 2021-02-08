# -*- coding: utf-8 -*-
# @Author : HUANG Mian
# @File : data.py

import pandas as pd

data_xls = pd.read_excel('Shenzhen.xlsx', index_col=0)
data_xls.to_csv('Shenzhen.csv', encoding='utf-8')
a=[]
Year=[]
Popu=[]
U_rate=[]
R_popu=[]
P_res=[]
with open("Shenzhen.csv",encoding='utf-8') as file:
    file.readline()
    for line in file:
        lst=[]
        row = line.strip().split(",")
        for item in row:
            lst.append(item)
        a.append(lst)

i=0
while i<len(a):
    Year.append(a[i][0]) #Year
    i+=1
i=0
while i<len(a):
    Popu.append(a[i][1]) #Population
    i+=1
i=0
while i<len(a):
    U_rate.append(a[i][2]) #U_rate
    i+=1
i=0
while i<len(a):
    R_popu.append(a[i][3]) #R_Popu
    i+=1
i=0
while i<len(a):
    P_res.append(a[i][4]) # P_Res
    i+=1

def get_factor(choice):
    if choice=="A":
        return Popu
    elif choice=="B":
        return U_rate
    elif choice=="C":
        return R_popu
    elif choice=="D":
        return P_res