from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
import requests
# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
page=requests.get(START_URL)
print(page)
Soup=bs(page.text,"html.parser")
start_table=Soup.find("table")
time.sleep(10)

planets_data = []
temp_list=[]
# Define Exoplanet Data Scrapping Method
table_rows=start_table[7].find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rsstrip() for i in td]
    temp_list.append(row)

star_name=[]
distance=[]
mass=[]
radius=[]
lum=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])



# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns=["Star_name","Distance","Mass","Radius","Luminosity"])
# Convert to CSV
planet_df_1.to_csv('scraped_data.csv')