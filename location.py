#%%
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt
import mysql.connector

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


ncr_cities = gpd.read_file('C:/Users/koben/Desktop/Projects/CPE106L-ProjectCovidRecon/ShapeFiles_NCR/Metropolitan Manila.shp')

for items in data_cases['country'].tolist():
    ncr_cities_list = ncr_cities['NAME_2'].tolist()

    if items in ncr_cities_list:
        pass
    else:
        print(items + ' is not in the NCR cities list')

ncr_cities.replace('Manila', 'City of Manila', inplace=True)
ncr_cities.replace('Kalookan City', 'Caloocan', inplace=True)
ncr_cities.replace('Makati City', 'Makati', inplace=True)
ncr_cities.replace('Pasay City', 'Pasay', inplace=True)
ncr_cities.replace('Pasig City', 'Pasig', inplace=True)

data_cases.rename(columns={'country':'City'}, inplace=True)
data_cases.rename(columns={'total_cases':'Total Cases'}, inplace=True)

#combined=ncr_cities.merge(data_cases, on= 'City')






# %%
