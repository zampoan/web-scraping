# ========================= 
#        PROJECT GOAL: 
# Webscrape and create a database of book name, price, author, descrption
# https://www.youtube.com/watch?v=MH3641s3Roc
# =========================
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# URL = "https://books.toscrape.com"
# r = requests.get(URL)
# # print(r.status_code) # returns 200 means ok

def extract(num_pages):
    title, star, price = [], [], []
    URL = "https://books.toscrape.com/catalogue/page-2.html"
    r = requests.get(URL)
    # print(r.status_code) # returns 200 means ok
    soup = BeautifulSoup(r.text, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title.append(image.attrs['alt'])
        stars = article.find('p')
        star.append(stars['class'][1])
        prices = article.find('p', class_='price_color').text
        price.append(float(prices[2:]))
    return title, star, price
        
def main():
    title, star, price = extract(50)
    print(title, star, price)

main()