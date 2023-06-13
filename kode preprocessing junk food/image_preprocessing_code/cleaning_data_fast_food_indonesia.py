#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:06:50 2023

@author: williamnehemia
"""

import pandas as pd

df = pd.read_csv('fast_food_indonesia.csv')

for index, row in df.iterrows():
    tipe = "string"
    #print(type(str))
    if (type(row['Menu']) != type(tipe)):
        print("ok")
        df = df.drop(index)
df = df.drop(columns = ['Unnamed: 0'])
df.to_csv('fast_food_indonesia_2.csv')