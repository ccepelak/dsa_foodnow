#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:49:00 2021

@author: angeladuarte
"""
#import required libraries

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import math
import random
import re
import geopandas as gpd


#%%


class RecommenderSystem:
    '''
     A class used to represent the recomender system
    ...

    Attributes
    ----------
    restaurant_list : list
        restaurants of the database
    user_input : str
       user preferences
    prepared_list : list
        creates a list of restaurants with user preferences
    cm : int
    cs: int
        centimeters closeness one to another
    scores: list
        enumeration of closeness
    sorted_scores: 
        ranking of restaurants 
            
    Methods
    -------
    prepare_list()
        creates a list with the restaurant features and user input
    get_similar_restaurants()
        uses cosine similarity to get the 10 more similar restaurants to the user input
    list_results()
        creates a list with the full information of the 10 most similar restaurants
    filter_best_ranked()
        filter the top 3 restaurants for the user input
    '''
    #Constructor
    def __init__(self, user_input):
        self.__restaurants= RestaurantList()
        self.__user_preference=user_input
        self.__prepared_list=[]
     
        
    #getters and setters:
    #returns the restaurant list.
    def getRestaurants(self):
        return self.__restaurants
    
    #returns the user preference
    def getUserInput(self):
        return self.__user_preference
    
    #returns the user preference.
    def getPreparedList(self):     
     return self.__prepared_list
 
    #returns the the restaurant features.
    def getRestaurantFeatures(self):
        features=self.getRestaurants().restaurantFeatures()
        return features
     
    #Sets a list with the user preferences and the restaurant features
    def setPreparedList(self):
        preparedList=self.getRestaurantFeatures()
        preparedList.append(self.getUserInput())
        preparedList.reverse()
        self.__prepared_list=preparedList

    #Uses cosine similarity to get the 10 more similar restaurants to the user input
    def get_similar_restaurants(self):
        cm=CountVectorizer().fit_transform(self.getPreparedList())
        cs=cosine_similarity(cm)
        scores=list(enumerate(cs[0]))
        sorted_scores=sorted(scores, key=lambda x:x[1], reverse=True)
        return sorted_scores[0:11]
    
    #Gets the indexes from the chosen restaurants on a list. 
    def getSelectedIndexes(self):
        indexes=[]
        for i in range(0,11):
           sorted_scores=self.get_similar_restaurants()
           selected_index=sorted_scores[i][0]
           indexes.append(selected_index)
        return indexes
        
    #Prints a list with the features of the 10 chosen restaurants. Helps to check
    #results. Probably will have to erase it later. 
    def list_results(self):
        results=[]
        for index in self.getSelectedIndexes():
           selected=self.getPreparedList()[index]
           results.append(selected)
        print(results)
    
    #Gets the selected restaurants into a list or Restaurants
    def getSelectedRestaurants(self):
        closest=[]
        indexes=self.getSelectedIndexes()[1:11]
        ones=[3438,3438,3438,3438,3438,3438,3438,3438,3438,3438]
        indexes2=np.subtract(ones,indexes).tolist()
        closest_features=[]
        for index in indexes2:
           restaurants_selected=self.getRestaurants().getRestaurantList()[index]
           closest.append(restaurants_selected)
           closest_features.append(restaurants_selected.getCuisine())
        print(closest_features)
        return closest
    
    #Filters the selected restaurants according to their ratings.
    def filter_best_ranked(self): 
        rest_list=self.getSelectedRestaurants()
        sorted_rest = sorted(rest_list, key=lambda x: x.getRating(), reverse=True)
        return sorted_rest[0:3]
        
    #Displays the 3 selected restaurants on a dictionary name: features.
    def outputResult(self):
        closest=self.filter_best_ranked()
        features={}
        for rest in closest: 
            features.update({rest.getName():rest.displayFeatures()})
        return features
        
        
        
        
#%%

#Testing the recommender system with some inputs. 
input2="International European Spicy luxury"

#Creating the recommender system
syst=RecommenderSystem(input2)
   
#running the required methods from the recommender system class
syst.setPreparedList()
syst.getPreparedList()
syst.get_similar_restaurants()
syst.list_results()     
syst.getSelectedIndexes()
syst.getSelectedRestaurants()
syst.filter_best_ranked()
syst.outputResult()

        
#%%
#Structure of the recommendation class, which will be used by the RecommenderSystem class
#to display outputs.  
class Recommendation:
    def __init__(self, output):
        self.output = output
        
    def display_output(self):
        print("The recommended restaurants are" + str(self.output))
    
    def plot_output(self):
        print("nothing yet!")
        
#%%