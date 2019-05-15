import sqlite3
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 
from customplot import * 
from sklearn.preprocessing import scale

# Ingestion 

cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)

cols = list(df.columns)
correlations = [] 
for f in cols:
    a = df['overall_rating'].corr(df[f])
    correlations.append(a)
print(len(correlations))

# Data Visualisation 

# Create a function which plots the with string columns and numeric values 

# def plot_dataframe(df, y_label):  
#     color='coral'
#     fig = plt.gcf()
#     fig.set_size_inches(20, 12)
#     plt.ylabel(y_label)

#     ax = df.correlation.plot(linewidth=3.3, color=color)
#     ax.set_xticks(df.index)
#     ax.set_xticklabels(df.attributes, rotation=75); #Notice the ; (remove it and see what happens !)
#     plt.show()

# df2 = pd.DataFrame({'attributes' : cols, 'correlation' : correlations})
# plot_dataframe(df2, 'Player Overall Rating')
