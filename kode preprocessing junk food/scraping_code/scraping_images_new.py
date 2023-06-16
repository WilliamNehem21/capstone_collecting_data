#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:43:58 2023

@author: williamnehemia
"""
# referensi https://serpapi.com/blog/scrape-google-images-with-python/


import requests, lxml, re, json, urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
import signal

dictionary = {}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
}

params = {
    "q": "big mac mcdonald", # search query
    "tbm": "isch",                # image results
    "hl": "en",                   # language of the search
    "gl": "us",                   # country where search comes from
    "ijn": "0"                    # page number
}

#html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
#soup = BeautifulSoup(html.text, "lxml")

def handle_timeout(signum, frame):
    raise TimeoutError

def get_images_with_request_headers(paramsIn):
    
    del params["ijn"]
    params["content-type"] = "image/png" # parameter that indicate the original media type

    return [img["src"] for img in soup.select("img")]

def get_suggested_search_data(paramsIn):
    print(paramsIn)
    
    suggested_searches = []

    all_script_tags = soup.select("script")

    
    matched_images = "".join(re.findall(r"AF_initDataCallback\(({key: 'ds:1'.*?)\);</script>", str(all_script_tags)))
    
    
    matched_images_data_fix = json.dumps(matched_images)
    matched_images_data_json = json.loads(matched_images_data_fix)

    
    suggested_search_thumbnails = ",".join(re.findall(r'{key(.*?)\[null,\"Size\"', matched_images_data_json))

    
    suggested_search_thumbnail_encoded = re.findall(r'\"(https:\/\/encrypted.*?)\"', suggested_search_thumbnails)

    for suggested_search, suggested_search_fixed_thumbnail in zip(soup.select(".PKhmud.sc-it.tzVsfd"), suggested_search_thumbnail_encoded):
        suggested_searches.append({
            "name": suggested_search.select_one(".VlHyHc").text,
            "link": f"https://www.google.com{suggested_search.a['href']}",
            
            "chips": "".join(re.findall(r"&chips=(.*?)&", suggested_search.a["href"])),
            
            "thumbnail": bytes(suggested_search_fixed_thumbnail, "ascii").decode("unicode-escape")
        })

    return suggested_searches

def get_original_images(folder_name, menu):

   

    google_images = []

    all_script_tags = soup.select("script")

    
    matched_images_data = "".join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))
    
    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    
    matched_google_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', matched_images_data_json)

    
    matched_google_images_thumbnails = ", ".join(
        re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                   str(matched_google_image_data))).split(", ")

    thumbnails = [
        bytes(bytes(thumbnail, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for thumbnail in matched_google_images_thumbnails
    ]

    
    removed_matched_google_images_thumbnails = re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', "", str(matched_google_image_data))

   
    matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_google_images_thumbnails)

    full_res_images = [
        bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for img in matched_google_full_resolution_images
    ]
    
    for index, (metadata, thumbnail, original) in enumerate(zip(soup.select('.isv-r.PNCib.MSM1fd.BUooTd'), thumbnails, full_res_images), start=1):
        try:
            link = metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["href"]
            google_images.append({
                "title": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["title"],
                "link": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["href"],
                "source": metadata.select_one(".fxgdke").text,
                "thumbnail": thumbnail,
                "original": original
            })
        except:
            print("error when getting the image")
        

        # Download original images
        print(f'Downloading {index} image...')
        
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36')]
        urllib.request.install_opener(opener)
        try:
            new_path = "/Users/williamnehemia/Documents/Bangkit-Course/download_image/clean_menu/" + folder_name + "/"
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            signal.signal(signal.SIGALRM, handle_timeout)
            signal.alarm(30)  # 5 seconds
            try:
                
                key = folder_name
                isi_before = dictionary.get(key)
                if (isi_before == None):
                    new_list = []
                    new_list.append(link)
                    dictionary[folder_name] = new_list
                    urllib.request.urlretrieve(original, f'{new_path}{menu}.{index}.jpg')
                else:
                    if(link not in isi_before):
                        isi_before.append(link)
                        dictionary[folder_name] = isi_before
                        urllib.request.urlretrieve(original, f'{new_path}{menu}.{index}.jpg')
                    
                    
            except:
                print("It took too long to finish the job")
            finally:
                signal.alarm(0)
        except:   
            print("http error")
            continue
        

    return google_images






df = pd.read_csv('fast_food_indonesia_cleaning_3.csv')
df = df.drop(columns = ['Unnamed: 0', 'Calories', 'Carbo', 'Protein', 'Fat'])
df = df.dropna()
Jenis = df['Jenis'].drop_duplicates()
print(Jenis)
indexStart = 0
for index, row in df.iterrows():
    if(row['Menu'] == 'Durian Balls Mountain Sundae' and row['Company'] == 'A&W Restaurants'):
        indexStart = index
        break
print(indexStart)

list_judul_ikut = ['Burger', 
                   'Wrap', 
                   'Rice bowl', 
                   'Fried chicken', 
                   'Ice cream', 
                   'Pastry', 
                   'Cupcake', 
                   'French Fries',
                   'Pasta',
                   'Pudding',
                   'Donuts',
                   'Pukis',
                   'Pizza',
                   'Stuffed pocket',
                   'Bread stick domino',
                   'Baked potato',
                   'Cookies',
                   'Waffle',
                   'Hot dog',
                   'Sandwich',
                   'Cake Jar', 
                   'Taco',
                   'Quesadilla', 
                   'Fish n chips'
                   
                   ]
#perlu tambah food
list_judul_ikut_edit = ['Circle pie', 
                        'Pocket wrap',
                        'Pita'
                        ]
"""
for index, row in df.iterrows():
    if(index >= indexStart):
        print("index", index)
        print(row['Menu'])
        if (row['Menu'] in list_judul_ikut):
            
            params = {
                "q": row['Menu'] + " " + row['Company'], # search query
                "tbm": "isch",                # image results
                "hl": "en",                   # language of the search
                "gl": "us",                   # country where search comes from
                "ijn": "0"                    # page number
            }
            html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
            soup = BeautifulSoup(html.text, "lxml")
            
            get_suggested_search_data(params)
            get_original_images(row['Jenis'], row['Menu'])
        
        elif(row['Menu'] in list_judul_ikut_edit):
            
            params = {
                "q": row['Menu'] + " " + row['Company'], # search query
                "tbm": "isch",                # image results
                "hl": "en",                   # language of the search
                "gl": "us",                   # country where search comes from
                "ijn": "0"                    # page number
            }
            html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
            soup = BeautifulSoup(html.text, "lxml")
            
            get_suggested_search_data(params)
            get_original_images(row['Jenis'], row['Menu'])
        else:
            params = {
                "q": row['Menu'] + " " + row['Company'], # search query
                "tbm": "isch",                # image results
                "hl": "en",                   # language of the search
                "gl": "us",                   # country where search comes from
                "ijn": "0"                    # page number
            }
            html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
            soup = BeautifulSoup(html.text, "lxml")
            
            get_suggested_search_data(params)
            get_original_images(row['Jenis'], row['Menu'])

for item in list_judul_ikut :
    params = {
        "q": item, # search query
        "tbm": "isch",                # image results
        "hl": "en",                   # language of the search
        "gl": "us",                   # country where search comes from
        "ijn": "0"                    # page number
    }
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    get_suggested_search_data(params)
    get_original_images(item, item)
"""
    
for item in list_judul_ikut_edit :
    params = {
        "q": item + " food", # search query
        "tbm": "isch",                # image results
        "hl": "en",                   # language of the search
        "gl": "us",                   # country where search comes from
        "ijn": "0"                    # page number
    }
    
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    get_suggested_search_data(params)
    get_original_images(item, item)    
            

    
