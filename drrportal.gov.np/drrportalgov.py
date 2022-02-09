# Python program to illustrate the concept
# of threading
import threading
import os

import requests
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np
from time import sleep
from random import randint





titles = []
rows1 = []
rows2 = []
rows3 = []
rows4 = []
rows5 = []
rows6 = []
rows7 = []
rows8 =[]

def scrape(n1,n2,lists,csv_title):
    pages = np.arange(n1, n2, 1)
    for page in pages:
        print("page:",page)
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
            row = data.find_all('td')
            for p in row:
                lists.append(p.text)

    for i in range(0,27):
        result[titles[i]]= list()

    n3 = (n2-n1)*10

    for i in range(0,n3):
        print('data:', i )
        for j in range(0,27):
            result[titles[j]].append(lists[27*i+j])

    drrportal_pd = pd.DataFrame(result)
    drrportal_pd.to_csv(str(csv_title)+'.csv')  



  

        
 

if __name__ == "__main__":

    result = dict()

	# creating threads
    t1 = threading.Thread(target=scrape,args = (1,360,rows1,'100_pages'), name='t1')
    t2 = threading.Thread(target=scrape, args = (360,720,rows2,'200_pages'), name='t2')
    t3 = threading.Thread(target=scrape, args = (720,1080,rows3,'300_pages'), name='t3')
    t4 = threading.Thread(target=scrape, args = (1080,1440,rows4,'400_pages') ,name='t4')
    t5 = threading.Thread(target=scrape,args = (1440,1800,rows5,'500_pages'), name='t5')
    t6 = threading.Thread(target=scrape,args = (1800,2120,rows6,'600_pages') ,name='t6')
    t7 = threading.Thread(target=scrape,args = (2120,2440,rows7,'700_pages') ,name='t7')
    t8 = threading.Thread(target=scrape,args = (2440,2858,rows8,'800_pages') ,name='t8')


	# starting threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()

	# wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()

    print("finished")


  
