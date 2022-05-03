import pandas as pd
import os

print(os.getcwd())
df1 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/100_pages.csv")
df2 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/200_pages.csv")
df3 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/300_pages.csv")
df4 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/400_pages.csv")
df5 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/500_pages.csv")
df6 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/600_pages.csv")
df7 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/700_pages.csv")
df8 = pd.read_csv("/home/chaos/Documents/GitHub/Web-Scraping/drrportal.gov.np/800_pages.csv")


frames = [df1,df2,df3,df4,df5,df6,df7,df8]
df3  = pd.concat(frames)
df3.to_csv("drrportal.csv")