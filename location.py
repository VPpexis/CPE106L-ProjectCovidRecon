#%%
import pandas as pd 
import matplotlib.pyplot as plt
import mysql.connector
import sys
import csv

data = mysql.connector.connect(
    host="myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com",
    user="myrds",
    passwd="admin123",
    database="myrds1"
)

cursor = data.cursor()
cursor.execute("SELECT * FROM temp")
result = cursor.fetchall()

df = pd.DataFrame(result, columns=['index','country','total_cases','total_deaths','total_recovered'])

data_cases = df[['country','total_cases']]

data_cases.rename(columns={'country':'City'}, inplace=True)
data_cases.rename(columns={'total_cases':'Total Cases'}, inplace=True)

c = csv.writer(open('dbdump01.csv', 'w'))
for x in result:
    c.writerow(x)

#combined=ncr_cities.merge(data_cases, on= 'City')






# %%
