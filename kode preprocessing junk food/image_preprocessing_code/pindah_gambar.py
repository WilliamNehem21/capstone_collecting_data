#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:14:47 2023

@author: williamnehemia
"""

import os
import random
import shutil

list_folder = ["Baked potato",
               "Burger",
               "Donut",
               "French fries",
               "Fried chicken"
               "Hotdog",
               "Pizza",
               "Sandwich",
               "Taco"]

dir_baked_potato = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Baked potato")
dir_burger = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Burger")
dir_donut = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Donut")
dir_french_fries = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/French fries")
dir_fried_chicken = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Fried chicken")
dir_hotdog = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Hotdog")
dir_pizza = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Pizza")
dir_sandwich = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Sandwich")
dir_taco = os.listdir("/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used/Taco")

dir_baked_potato.sort()
dir_burger.sort()
dir_donut.sort()
dir_french_fries.sort()
dir_fried_chicken.sort()
dir_hotdog.sort()
dir_pizza.sort()
dir_sandwich.sort()
dir_taco.sort()

random.seed(0)

random.shuffle(dir_baked_potato)
random.shuffle(dir_burger)
random.shuffle(dir_donut)
random.shuffle(dir_french_fries)
random.shuffle(dir_fried_chicken)
random.shuffle(dir_hotdog)
random.shuffle(dir_pizza)
random.shuffle(dir_taco)


split_1 = int(0.75 * 150)
split_2 = int(0.95 * 150)

train_dir_baked_potato = dir_baked_potato[:split_1]
test_dir_baked_potato = dir_baked_potato[split_1:split_2]
val_dir_baked_potato = dir_baked_potato[split_2:]

train_dir_burger = dir_burger[:split_1]
test_dir_burger = dir_burger[split_1:split_2]
val_dir_burger = dir_burger[split_2:]

train_dir_donut = dir_donut[:split_1]
test_dir_donut = dir_donut[split_1:split_2]
val_dir_donut = dir_donut[split_2:]

train_dir_french_fries = dir_french_fries[:split_1]
test_dir_french_fries = dir_french_fries[split_1:split_2]
val_dir_french_fries = dir_french_fries[split_2:]

train_dir_fried_chicken = dir_fried_chicken[:split_1]
test_dir_fried_chicken = dir_fried_chicken[split_1:split_2]
val_dir_fried_chicken = dir_fried_chicken[split_2:]


train_dir_hotdog = dir_hotdog[:split_1]
test_dir_hotdog = dir_hotdog[split_1:split_2]
val_dir_hotdog = dir_hotdog[split_2:]


train_dir_pizza = dir_pizza[:split_1]
test_dir_pizza = dir_pizza[split_1:split_2]
val_dir_pizza = dir_pizza[split_2:]


train_dir_sandwich = dir_sandwich[:split_1]
test_dir_sandwich = dir_sandwich[split_1:split_2]
val_dir_sandwich = dir_sandwich[split_2:]


train_dir_taco = dir_taco[:split_1]
test_dir_taco = dir_taco[split_1:split_2]
val_dir_taco = dir_taco[split_2:]


src_dir = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/will_be_used"
train_dir = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/Fast Food Classification V2/Train/"
test_dir = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/Fast Food Classification V2/Test/"
val_dir = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/Fast Food Classification V2/Valid/"

for file in train_dir_baked_potato:
    srcpath = os.path.join(src_dir, "Baked potato/"  + file)
    shutil.copy(srcpath, train_dir + "Baked potato" )

for file in test_dir_baked_potato:
    srcpath = os.path.join(src_dir, "Baked potato/" + file)
    shutil.copy(srcpath, test_dir + "Baked potato" )

for file in val_dir_baked_potato:
    srcpath = os.path.join(src_dir,"Baked potato/" + file)
    shutil.copy(srcpath, val_dir + "Baked potato" )



for file in train_dir_burger:
    srcpath = os.path.join(src_dir, "Burger/" + file)
    shutil.copy(srcpath, train_dir + "Burger" )

for file in test_dir_burger:
    srcpath = os.path.join(src_dir, "Burger/" + file)
    shutil.copy(srcpath, test_dir + "Burger" )

for file in val_dir_burger:
    srcpath = os.path.join(src_dir, "Burger/" + file)
    shutil.copy(srcpath, val_dir + "Burger" )
    
    
    
for file in train_dir_donut:
    srcpath = os.path.join(src_dir, "Donut/"  + file)
    shutil.copy(srcpath, train_dir + "Donut" )

for file in test_dir_donut:
    srcpath = os.path.join(src_dir, "Donut/"  + file)
    shutil.copy(srcpath, test_dir + "Donut" )

for file in val_dir_donut:
    srcpath = os.path.join(src_dir, "Donut/"  + file)
    shutil.copy(srcpath, val_dir + "Donut" )



for file in train_dir_french_fries:
    srcpath = os.path.join(src_dir, "French fries/" + file)
    shutil.copy(srcpath, train_dir + "French fries" )

for file in test_dir_french_fries:
    srcpath = os.path.join(src_dir, "French fries/" + file)
    shutil.copy(srcpath, test_dir + "French fries" )

for file in val_dir_french_fries:
    srcpath = os.path.join(src_dir, "French fries/" + file)
    shutil.copy(srcpath, val_dir + "French fries" )



for file in train_dir_fried_chicken:
    srcpath = os.path.join(src_dir, "Fried chicken/" + file)
    shutil.copy(srcpath, train_dir + "Fried chicken" )

for file in test_dir_fried_chicken:
    srcpath = os.path.join(src_dir, "Fried chicken/" + file)
    shutil.copy(srcpath, test_dir + "Fried chicken" )

for file in val_dir_fried_chicken:
    srcpath = os.path.join(src_dir, "Fried chicken/" + file)
    shutil.copy(srcpath, val_dir + "Fried chicken" )



for file in train_dir_hotdog:
    srcpath = os.path.join(src_dir, "Hotdog/" + file)
    shutil.copy(srcpath, train_dir + "Hotdog" )

for file in test_dir_hotdog:
    srcpath = os.path.join(src_dir, "Hotdog/" + file)
    shutil.copy(srcpath, test_dir + "Hotdog" )

for file in val_dir_hotdog:
    srcpath = os.path.join(src_dir, "Hotdog/" + file)
    shutil.copy(srcpath, val_dir + "Hotdog" )


for file in train_dir_pizza:
    srcpath = os.path.join(src_dir, "Pizza/" + file)
    shutil.copy(srcpath, train_dir + "Pizza" )

for file in test_dir_pizza:
    srcpath = os.path.join(src_dir, "Pizza/" + file)
    shutil.copy(srcpath, test_dir + "Pizza" )

for file in val_dir_pizza:
    srcpath = os.path.join(src_dir, "Pizza/" + file)
    shutil.copy(srcpath, val_dir + "Pizza" )





for file in train_dir_sandwich:
    srcpath = os.path.join(src_dir, "Sandwich/" + file)
    shutil.copy(srcpath, train_dir + "Sandwich" )

for file in test_dir_sandwich:
    srcpath = os.path.join(src_dir, "Sandwich/" + file)
    shutil.copy(srcpath, test_dir + "Sandwich" )

for file in val_dir_sandwich:
    srcpath = os.path.join(src_dir, "Sandwich/" + file)
    shutil.copy(srcpath, val_dir + "Sandwich" )




for file in train_dir_taco:
    srcpath = os.path.join(src_dir, "Taco/" + file)
    shutil.copy(srcpath, train_dir + "Taco" )

for file in test_dir_taco:
    srcpath = os.path.join(src_dir, "Taco/" + file)
    shutil.copy(srcpath, test_dir + "Taco" )

for file in val_dir_taco:
    srcpath = os.path.join(src_dir, "Taco/" + file)
    shutil.copy(srcpath, val_dir + "Taco" )

