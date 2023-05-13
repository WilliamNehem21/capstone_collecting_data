#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:56:44 2023

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




#df = pd.DataFrame()
#df['Company'] = ''
#df['Menu'] = ''

mydict = {'Company' : [], 'Menu' : []}


# mcd
driver = webdriver.Chrome()
url = "https://mcdonalds.co.id/menu"
menu_list = []
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
p_tags =  driver.find_elements(By.TAG_NAME, "p") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('McDonald\'s')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #mydict['Company'] = company_dict
        #mydict['Menu'] = menu_dict
        #dict = {'Company': 'McDonald\'s', 'Menu' : menu_name}
        #df2 = pd.DataFrame(dict)
        #df = pd.concat([df, df2], ignore_index = True)
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['McDonald\'s', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver




# kfc
driver = webdriver.Chrome()
url = "https://kfcku.com/food"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "span.zoom--item") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('KFC')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'KFC', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['KFC', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#pizza hut

driver = webdriver.Chrome()
url = "https://www.pizzahut.co.id/digital-menu"
menu_list = []
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
p_tags =  driver.find_elements(By.TAG_NAME, "h3") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Pizza Hut')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Pizza Hut', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Pizza Hut', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver



#phd
driver = webdriver.Chrome()
url = "https://www.pizzahut.co.id/digital-menu/phd"
menu_list = []
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
p_tags =  driver.find_elements(By.TAG_NAME, "h3") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        
        
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('PHD')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'PHD', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['PHD', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#domino pizza

driver = webdriver.Chrome()
url = "https://www.dominos.co.id/sides-desserts"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "h2.product-name") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_name = menu_name.removeprefix("NEW! ")
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Domino\'s Pizza')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Domino\'s Pizza', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Domino\'s Pizza', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


driver = webdriver.Chrome()
url = "https://www.dominos.co.id/pizza"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "h2.product-name") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_name = menu_name.removeprefix("NEW! ")
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Domino\'s Pizza')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Domino\'s Pizza', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Domino\'s Pizza', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


# burger king
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/burger-king-skyline-delivery/IDGFSTI000004qy"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Burger King')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Burger King', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Burger King', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


# wendy's
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/wendy-s-menara-bank-mega-food-court-jakarta-delivery/IDGFSTI000022ds"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Wendy\'s')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Wendy\'s', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Wendy\'s', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#carl's jr
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/carl-s-jr-burger-ayam-darmo-delivery/IDGFSTI00000jdo"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Carl\'s Jr.')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Carl\'s Jr.', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Carl\'s Jr.', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#J.co

driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/j-co-donuts-coffee-plaza-atrium-delivery/IDGFSTI000022v8"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('J.CO Donuts & Coffee')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'J.CO Donuts & Coffee', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['J.CO Donuts & Coffee', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#starbucks
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/starbucks-sabang-delivery/6-C2U3DBLHLUEHJE"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Starbucks')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Starbucks', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Starbucks', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#dunkin donuts
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/dunkin-donuts-menteng-delivery/IDGFSTI000023an"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Dunkin\' Donuts')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Dunkin\' Donuts', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Dunkin\' Donuts', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#baskin robins
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/baskin-robbins-mall-taman-anggrek-delivery/6-C2VYJVBEJKBCTN"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Baskin-Robbins')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Baskin-Robbins', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Baskin-Robbins', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


# cold stone
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/cold-stone-ice-cream-grand-indonesia-delivery/IDGFSTI000024c5"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Cold Stone')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Cold Stone', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Cold Stone', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#dairy queen

driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/dairy-queen-grand-indonesia-mall-delivery/6-CZNTHBMYMFLFGT"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Dairy Queen')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Dairy Queen', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Dairy Queen', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#pizza marzano
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/pizza-marzano-grand-indonesia-delivery/IDGFSTI000002y2"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Pizza Marzano')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Pizza Marzano', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Pizza Marzano', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#texas chicken
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/texas-chicken-rawa-belong-delivery/6-C3X1C23GPFUDRT"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Texas Chicken')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Texas Chicken', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Texas Chicken', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

# popeye
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/popeyes-skyline-delivery/6-C32KCBBWV3BDTT"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Popeyes Louisiana Kitchen')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Popeyes Louisiana Kitchen', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Popeyes Louisiana Kitchen', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#A&W
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/a-w-hayam-wuruk-delivery/6-CYNCG2XJUGNJJT"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('A&W Restaurants')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'A&W Restaurants', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['A&W Restaurants', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#shilin
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/shihlin-taiwan-street-snacks-grand-indonesia-delivery/IDGFSTI000005pk"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Shihlin Taiwan Street Snacks')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Shihlin Taiwan Street Snacks', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Shihlin Taiwan Street Snacks', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#cfc
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/cfc-tanah-abang-blok-a-delivery/6-C35XRCK1LELXG2"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('CFC')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'CFC', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['CFC', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver


#coffee bean
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/the-coffee-bean-tea-leaf-uob-plaza-delivery/IDGFSTI000035w2"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('The Coffee Bean & Tea Leaf')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'The Coffee Bean & Tea Leaf', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['The Coffee Bean & Tea Leaf', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#doner kebab
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/doner-kebab-grand-indonesia-delivery/IDGFSTI0000239x"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Doner Kebab')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Doner Kebab', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Doner Kebab', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#krispy kreme
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/krispy-kreme-harmoni-exchange-delivery/6-C35KN35XCA4HG2"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Krispy Kreme')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Krispy Kreme', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Krispy Kreme', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#wingstop
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/wingstop-grand-indonesia-delivery/6-CYTWMA5ARNDVCN"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Wingstop')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Wingstop', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Wingstop', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver

#Richeese Factory
driver = webdriver.Chrome()
url = "https://food.grab.com/id/id/restaurant/richeese-factory-lokasari-delivery/IDGFSTI000020vs"
menu_list = []
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
p_tags =  driver.find_elements(By.CSS_SELECTOR, "p.itemNameTitle___1sFBq") #ambil semua tag img

counter = 1

print(len(p_tags), "jumlah tag img")
for p_tag in p_tags:
    try:
        menu_name = p_tag.text
        menu_list.append(menu_name)
        company_dict = mydict.get('Company')
        company_dict.append('Richeese Factory')
        menu_dict = mydict.get('Menu')
        menu_dict.append(menu_name)
        mydict.update( {'Company' : company_dict, 'Menu' : menu_dict})
        #df2 = {'Company': 'Richeese Factory', 'Menu' : menu_name}
        #df = df.append(df2, ignore_index = True)
        #df.append(pd.Series(['Richeese Factory', menu_name ]), ignore_index=True)
        
    except:
        print("no alt attribute")
print(menu_list)
driver.close() 
driver.quit() #tutup webdriver
df = pd.DataFrame(mydict)
print(df)
df.to_csv('fast_food_indonesia.csv')
