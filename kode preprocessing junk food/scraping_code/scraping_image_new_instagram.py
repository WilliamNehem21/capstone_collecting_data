#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:12:56 2023

@author: williamnehemia
"""

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
    name = name.replace("'s", "")
    name = name.replace("s", "")
    name = name.lower()
    list2 = name.split(" ")
    for item in list1:
        item = item.lower()
        item = item.replace("s", "")
        if(item not in list2):
            flag = False
            break
    return flag





#df = pd.read_csv("fastfood.csv")
#df["search"] = df["item"] + " " + df["restaurant"]

df = pd.read_csv("menu_to_search.csv")
df["search"] = df["Menu"] + df["Company"]


for index, row in df.iterrows():
    driver = webdriver.Chrome()
    #url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiUweC0wef-AhXg9zgGHTRfCBsQ_AUoAXoECAEQAw&biw=882&bih=740&dpr=2"
    #url = "https://www.pinterest.com/search/pins/?rs=ac&len=2&q={}"
    url = "https://www.instagram.com/explore/tags/{}/"
    search = row["search"]
    search = search.replace(".", "")
    search = search.replace("'", "")
    search = search.replace("&", "")
    search = search.replace(" ", "")
    search = search.lower()
    search_list = search.split(" ")
    #search_url = "+".join(search_list)
    #search_url = "%20".join(search_list)
    
    search_check_list = search_list[:len(search_list)-1]
    url = url.format(search)
    print(url)
    driver.get(url) #buka halaman google image sesuai pencarian
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    img_tags =  driver.find_elements(By.TAG_NAME, "img") #ambil semua tag img
    counter = 1
    #path = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/menu_to_search/google" #path simpan ke folder mana
    #path = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/menu_to_search/pinterest"
    path = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/menu_to_search/instagram"
    print(len(img_tags), "jumlah tag img")
    for img_tag in img_tags:
        try:
            image_name = img_tag.get_attribute("alt")
            image_name = image_name.lower()
            source_image = img_tag.get_attribute("src")
            print(img_tag.get_attribute("alt"))
            if((not source_image == "none") and source_image is not None):
                download_image(source_image,path, str(counter), search)
                counter += 1
            #if(check_list_in_name(search_check_list, image_name) == True):
                
        except:
            print("no alt attribute")
    driver.close() 
    driver.quit() #tutup webdriver

       
    
    




