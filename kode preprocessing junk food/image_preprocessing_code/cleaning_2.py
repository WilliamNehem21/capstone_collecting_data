#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:58:50 2023

@author: williamnehemia
"""

import pandas as pd

df = pd.read_csv('fast_food_indonesia_2.csv')
delete_list = ["ice", "iced", "hot", "float", "tea", "latte", "frappe", "sprite", "coca cola", "fanta", "combo", "kombo", "paket", "family", "coke", "box", "sauce", "teh", "kopi", "dip", "mineral"]

for index, row in df.iterrows():
    for item in delete_list:
        menu = row["Menu"]
        menu = menu.lower()
        if(item in menu):
            df = df.drop(index)
            break
df = df.drop(columns = ['Unnamed: 0'])
df.to_csv("fast_food_indonesia_cleaning_2.csv")