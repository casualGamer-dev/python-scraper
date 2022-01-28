from bs4 import BeautifulSoup
import requests
import time
import pandas as pd 
import os
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table", {"class": "wikitable sortable"})
print(page)
templist=[]
tablerows=table.find_all("tr")
for tr in tablerows:
    td =tr.find_all("td")
    row=[i.text.strip() for i in td]
    templist.append(row)
print(templist)
starnames=[]
distance=[]
radius=[]
mass=[]
luminosity=[]
for i in range (1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    radius.append(templist[i][6])
    mass.append(templist[i][5])
    luminosity.append(templist[i][7]) 
df2=pd.DataFrame({"Star Name":starnames,"Distance":distance,"Radius":radius,"Mass":mass,"Luminosity":luminosity})
df2.to_csv("star_data.csv")
print(df2)
time.sleep(15)


        