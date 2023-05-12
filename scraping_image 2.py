#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:29:59 2023

@author: williamnehemia
"""



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os
import pandas as pd

def download_image(url, file_path, file_name, folder_name):
    new_path = file_path + "/" + folder_name + "/"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    full_path = new_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

def check_list_in_name(list1, name):
    flag = True
    name = name.replace("®", "")
    list2 = name.split(" ")
    for item in list1:
        if(item in list2):
            flag = False
            break
    return flag

driver = webdriver.Chrome()



df = pd.read_csv("fastfood.csv")
df["search"] = df["item"] + " " + df["restaurant"]

for index, row in df.iterrows():
    url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiUweC0wef-AhXg9zgGHTRfCBsQ_AUoAXoECAEQAw&biw=882&bih=740&dpr=2"
    search = row["search"]
    search_list = search.split(" ")
    search_url = "+".join(search_list)
    url = url.format(search_url)
    print(url)
    driver.get(url) #buka halaman google image sesuai pencarian
    img_tags =  driver.find_elements(By.TAG_NAME, "img") #ambil semua tag img
    counter = 1
    path = "/Users/williamnehemia/Documents/Bangkit-Course/download_image" #path simpan ke folder mana

    for img_tag in img_tags:
        image_name = img_tag.get_attribute("alt")
        if(check_list_in_name(search_list, image_name) == True):
            source_image = img_tag.get_attribute("src")
            print(img_tag.get_attribute("alt"))
            if((not source_image == "none") and source_image is not None):
                download_image(source_image,path, str(counter), search)
                counter += 1
                



    
driver.close() 
driver.quit() #tutup webdriver


