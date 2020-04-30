#%%
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt
import mysql.connector

#Connects to the db server
data = mysql.connector.connect(
    host="myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com",
    user="myrds",
    passwd="admin123",
    database="myrds1"
)

cursor = data.cursor()
cursor.execute("SELECT * FROM temp")
result = cursor.fetchall()

#Imports data from db and place it to a table
df = pd.DataFrame(result, columns=['index','country','total_cases','total_deaths','total_recovered'])
df.rename(columns={'country':'City','total_cases':'Total Cases'}, inplace=True)
data_cases = df[['City','Total Cases']]

#Imports the map and changes the headers
ncr_cities = gpd.read_file('ShapeFiles_NCR/Metropolitan Manila.shp')
ncr_cities.rename(columns={'NAME_2':'City'}, inplace=True)

#Changes the Cities name.
ncr_cities.replace('Manila', 'City of Manila', inplace=True)
ncr_cities.replace('Kalookan City', 'Caloocan', inplace=True)
ncr_cities.replace('Makati City', 'Makati', inplace=True)
ncr_cities.replace('Pasay City', 'Pasay', inplace=True)
ncr_cities.replace('Pasig City', 'Pasig', inplace=True)


for items in data_cases['City'].tolist():
    ncr_cities_list = ncr_cities['City'].tolist()

    if items in ncr_cities_list:
        pass
    else:
        print(items + ' is not in the NCR cities list')


#ncr_cities.to_csv('temp.txt')



#combined=ncr_cities.merge(data_cases, on= 'City')






# %%
