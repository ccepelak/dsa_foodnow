
#author: @ccepelak

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import math
import random
import re
import geopandas as gpd

class User_Preference:
  def __init__(self, name, cuisine_style, price_range, ranking, distance):
    self.name = name
    self.cuisine = cuisine_style
    self.price = price_range
    self.ranking = ranking
    self.distance = distance

  def setName(self):
    return self.name

  def cleanCuisineStyle(self, cuisine_style):
    self.cuisine_style = self.cuisine_style.replace(" ", ",")
    return self.cuisine_style
  
  #def setCuisineStyle(self):
    #return self.cuisine_style

  def getCuisineStyle(self):
    return self.cuisine_style

  def getPrice(self):
    return self.price_range

  def getRanking(self):
    return self.ranking

  def getDistance(self):
    return self.distance
