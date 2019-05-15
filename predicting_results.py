# In this part, we analyse the results and try to predict the overall rating of the player

import sqlite3
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale 
from customplot import * 

# Importing data 

cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)

print(df.head(5))
# randomise data 
# df = df.reindex(np.random.permutation(df.index))

# Most of the time, we are only interested in plotting some columns. 
# In that case, we can use the pandas column selection option as follows. 

print(df[:10][['penalties', 'overall_rating']])

# Correlation Analysis 
# print(df['overall_rating'].corr(df['penalties']))

potentialFeatures = ['acceleration', 'curve', 'free_kick_accuracy', 'ball_control', 'shot_power', 'stamina']

# check how the features are correlated with the overall ratings
for f in potentialFeatures:
    related = df['overall_rating'].corr(df[f])
    print("%s: %f" % (f,related))
