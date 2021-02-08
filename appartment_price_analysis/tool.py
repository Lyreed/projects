# -*- coding: utf-8 -*-
# @Author : HUANG Mian
# @File : tool.py

import matplotlib.pyplot as plt

class Graph:
    """Presenting the data with scatter diagram"""

    def __init__(data,factor1,factor2):
        data.f1=factor1
        data.f2=factor2

    def graph1(data):
        plt.figure(figsize=(10,10))
        plt.scatter(data.f1,data.f2,label='plt')
        plt.title(u"Population in recent years",size=10)
        plt.xlabel(u'Year',size=10)
        plt.ylabel(u'Population',size=10)
        plt.legend()
##        plt.savefig("C:\\Users\\hmian\\Desktop\\project\\result1.jpg")    # Save the figure
        plt.show()

    def graph2(data):
        plt.figure(figsize=(10,10))
        plt.scatter(data.f1,data.f2,label='plt')
        plt.title(u"Urbanization rate in recent years",size=10)
        plt.xlabel(u'Year',size=10)
        plt.ylabel(u'urbanization rate',size=10)
        plt.legend()
##        plt.savefig("C:\\Users\\hmian\\Desktop\\project\\result2.jpg")
        plt.show()

    
    def graph3(data):
        plt.figure(figsize=(10,10))
        plt.scatter(data.f1,data.f2,label='plt')
        plt.title(u"Resident population in recent years",size=10)
        plt.xlabel(u'Year',size=10)
        plt.ylabel(u'urbanization rate',size=10)
        plt.legend()
##        plt.savefig("C:\\Users\\hmian\\Desktop\\project\\result3.jpg")
        plt.show()

    def graph4(data):
        plt.figure(figsize=(10,10))
        plt.scatter(data.f1,data.f2,label='plt')
        plt.title(u"Permanent population in recent years",size=10)
        plt.xlabel(u'Year',size=10)
        plt.ylabel(u'Permanent population',size=10)
        plt.legend()
##        plt.savefig("C:\\Users\\hmian\\Desktop\\project\\result4.jpg")
        plt.show()

    



     


