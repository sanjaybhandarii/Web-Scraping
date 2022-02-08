import requests
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np
from time import sleep
from random import randint


pages = np.arange(1, 2, 1)


titles = []
prices = []
in_stock = []
star_ratings = []


for page in pages:
    res = requests.get('http://drrportal.gov.np/incidentreport/index_ajax/'+ str(page) + '.html')
    
    soup = BeautifulSoup(res.text,'lxml')
    columns = soup.find_all('th')
    #sleep(randint(2,10))
    
    
    for column in columns:

        title = column.text
        titles.append(title)

    body = soup.find('tbody')
    
    datas = body.find_all('tr')

    for data in datas:
        price = data.find_all('td')
        for p in price:
            prices.append(p.text)



result = dict()

for i in range(0,27):
    result[titles[i]]= list()

  

for i in range(0,10):

    for j in range(0,27):
        result[titles[j]].append(prices[27*i+j])

print(result)

        

        
            
#         books = pd.DataFrame({
#             'title': titles,
#             'Price': prices,
#             'In_Stock': in_stock,
#             'Star_ratings':star_ratings,
#             })
        
#         books['Price'] = books['Price'].str.extract('(\d+.\d+)').astype(float)
        
# books.to_csv("books_scraped.csv")