# ========================= 
#        PROJECT GOAL: 
# Webscrape and create a database of book name, price, author, descrption
# =========================
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

title = []

URL = "https://books.toscrape.com"
r = requests.get(URL)
print(r.status_code) # returns 200 means ok

def extract():
    soup = BeautifulSoup(r.text, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title.append(image.attrs['alt'])
        
    return title
        
