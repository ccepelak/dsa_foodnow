# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:13:54 2021

@author: bakic
"""

import pandas as pd

#Preparing the data
df = pd.read_csv("Data/TA_restaurants_curated.csv")

#filter restaurants in Berlin
df_Berlin=df[df.City=="Berlin"]
df_Berlin.head(5)

df_Berlin.shape

columns=["Name", "Cuisine Style", "Ranking", "Rating", "Price Range", "Number of Reviews"]
df[columns].head(5)

#Dropping NA'S and reseting index. Storing the info in a dataframe called df_berlin
df_berlin=df_Berlin.dropna()
df_berlin.reset_index(drop=True, inplace=True)

##needed to be able to run restaurant class for now, until we sort out white space
#stripping white space
df_berlin.columns = [c.replace(' ', '_') for c in df_berlin.columns]
