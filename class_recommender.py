#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:49:00 2021

@author: angeladuarte
"""

#package import
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from class_restaurantlist import RestaurantList


#%%


class RecommenderSystem:
    #Constructor
    def __init__(self, user_preference):
        self.__restaurants= RestaurantList()
        self.__user_preference=user_preference
        self.__prepared_list=[]
    #Prints a string when it is asked to print an instance of this class
    def __str__(self):
        return 'This is a Cosine Similarity recommender system. With input {}'.format(self.getUserInput())    
        
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
           closest_features.append(restaurants_selected.displayCuisine())
        return closest
    
    #Filters the selected restaurants according to their ratings.
    def filter_best_ranked(self): 
        rest_list=self.getSelectedRestaurants()
        sorted_rest = sorted(rest_list, key=lambda x: x.getRating(), reverse=True)
        return sorted_rest[0:3]
        
    #Displays the 3 selected restaurants using the displayRestaurant() method from the restaurantClass.
    def outputResult2(self):
        closest=self.filter_best_ranked()
        f = ""
        no = 1
        print("Your matches are:")
        for rest in closest:
            f = str(no) + ". " + rest.displayRestaurant() 
            no += 1
            print(f)
            
#%%

if __name__=='__main__':
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
    syst.outputResult2()
    print(syst)