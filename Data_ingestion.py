import sqlite3
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale 
from customplot import * 

# Step 1: Data Ingestion 

cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx) 
# here pandas reads the data from the database and stores it in a dataframe 

# Step 2: Exploring Data - Gener ating simple statistics out of our data 
print(df.columns)
print(df.describe().transpose())

# Step 3: Data Cleaning - Handling Missing Data 
print(df.isnull())
print(df.isnull().any().any()) 
print(df.isnull().sum())

# Fixing null values by deleting them

#Take inital number of rows 
row = df.shape[0]

#Drop the null rows 
df = df.dropna()
print(df.isnull().sum())

