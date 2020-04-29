#%%
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt
import mysql.connector



data = mysql.connector.connect(
    host="myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com",
    user="myrds",
    passwd="admin123",
    database="myrds1",
)

cursor = data.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)


#ncr_cities = gpd.read_file('C:/Users/koben/Desktop/Projects/CPE106L-ProjectCovidRecon/Metropolitan Manila/Metropolitan Manila.shp')

#ncr_cities.plot()

#print(data)

print(data)