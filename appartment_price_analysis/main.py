# -*- coding: utf-8 -*-
# @Author : HUANG Mian, LE Yao
# @File : main.py

from tool import Graph
from data import Year, get_factor
from analysis import avgprice_bar, yearbuilt_pie, layout_pie, priceOfApartment
from input import district_input, layout_input, direction_input, metro_input

flag = True
while flag:
    print("-------------------------------------------------------------")
    num = int(input("Please enter 1 if you want information about population and urbanization\n"
                    "Enter 2 if you want general information about price of apartments in Shenzhen city.\n"
                    "Enter 3 if you want information about year built.\n"
                    "Enter 4 if you want information about layout.\n"
                    "Enter 5 if you want information about average price of different types of apartments.\n"
                    "Enter 0 if you want to quit.\n"
                    "Your input: "))
    print("-------------------------------------------------------------")
    if num == 0:
        break

    elif num == 1:
        print("You choice:")
        print()
        print("A:Population  B:Urbanization rate")
        print()
        print("C: Resident population  D: Permanent population")
        print()
        choice1 = input("Select your data : ")

        factor1 = Year
        factor2 = get_factor(choice1)

        g = Graph(factor1, factor2)
        if choice1 == "A":
            g.graph1()
        elif choice1 == "B":
            g.graph2()
        elif choice1 == "C":
            g.graph3()
        elif choice1 == "D":
            g.graph4()
        print("----------------------------")

    elif num == 2:
        file = "average_price.html"
        avgprice_bar().render(file)
        print("An html file - \"{}\" is generated in your current working directory.".format(file))
        print("-------------------------------------------------------------")

    elif num == 3:
        district = district_input()
        if district == "invalid input":
            continue
        pie = yearbuilt_pie(district)
        if pie == "invalid input":
            print("Invalid Input.")
            print("----------------------------")
        else:
            file = "yearBuilt_{}.html".format(district)
            pie.render(file)  # generate an html file
            print("An html file - \"{}\" is generated in your current working directory.".format(file))
            print("-------------------------------------------------------------")

    elif num == 4:
        district = district_input()
        if district == "invalid input":
            continue
        pie = layout_pie(district)
        if pie == "invalid input":
            print("Invalid Input.")
            print("----------------------------")
        else:
            file = "layout_{}.html".format(district)
            pie.render(file)  # generate an html file
            print("An html file - \"{}\" is generated in your current working directory.".format(file))
            print("-------------------------------------------------------------")

    elif num == 5:
        district = district_input()
        layout = layout_input()
        nearMetro = metro_input()
        direction = direction_input()
        if district == "invalid input" or direction == "invalid input" or \
                        layout == "invalid input" or nearMetro == "invalid input":
            continue

        priceOfApartment(district, layout, nearMetro, direction)

    i = input("If you want to quit, Please enter 0.\n"
              "Otherwise please enter 1.\n"
              "input: ")
    i = int(i)
    if i == 0:
        flag = False





        
            
            
            
    


















