#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: angeladuarte, ccpelak, bakic, egracialeon

This script allows the user to input his/her restaurant preferences to the
recommender system. The program will output the restaurants with the most 
similar features to those of the user has input.

This program accepts input as a string/list

The script requieres , `numpy`, cosine_similarity from `sklearn.metrics.pairwise´, 
CountVectorizer from ´sklearn.feature_extraction.text´ and the class RestaurantList from the
class_restaurantlist

This file can also be imported as a module and contains the following
functions:
    
    getRestaurants()
        Returns the restaurant list
    getUserInput()
        Returns the user preference
    getPreparedList()
        Returns the user preference
    getRestaurantFeatures()
        Returns the the restaurant features
    setPreparedList()
        Sets a list with the user preferences and the restaurant features
    get_similar_restaurants()
        Uses cosine similarity to get the 10 more similar restaurants to the user input
    get_selected_indexes()
        Gets the indexes from the chosen restaurants on a list
    list_results()
        Prints a list with the features of the 10 chosen restaurants. Helps to check
    get_selected_restaurants()
        Gets the selected restaurants into a list or Restaurants
    filter_best_ranked()
        Filters the selected restaurants according to their ratings
    outputResult()
        Displays the 3 selected restaurants on a dictionary name: features

    
"""

#package import
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from class_restaurantlist import RestaurantList


#%%


class RecommenderSystem:
        '''
     A class used to represent the recomender system algorithm
    

    Attributes
    ----------
    restaurants:
        restaurants list 
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
    getRestaurants()
        Returns the restaurant list
    getUserInput()
        Returns the user preference
    getPreparedList()
        Returns the user preference
    getRestaurantFeatures()
        Returns the the restaurant features
    setPreparedList()
        Sets a list with the user preferences and the restaurant features
    get_similar_restaurants()
        Uses cosine similarity to get the 10 more similar restaurants to the user input
    get_selected_indexes()
        Gets the indexes from the chosen restaurants on a list
    list_results()
        Prints a list with the features of the 10 chosen restaurants. Helps to check
    get_selected_restaurants()
        Gets the selected restaurants into a list or Restaurants
    filter_best_ranked()
        Filters the selected restaurants according to their ratings
    outputResult()
        Displays the 3 selected restaurants on a dictionary name: features
    '''
    #Constructor
        def __init__(self, user_preference):
            '''
        This is the constructor of the class Recomender System
        
        Parameters
        ----------
    restaurants: list
        restaurants list 
    user_input : str
        user preferences
    prepared_list : list
        creates a list of restaurants with user preferences
        '''
            self.__restaurants= RestaurantList()
            self.__user_preference=user_preference
            self.__prepared_list=[]
    #Prints a string when it is asked to print an instance of this class
        def __str__(self):
            '''
            Prints a string when it is asked to print an instance of this class
    
            Returns
            -------
            'This is a Cosine Similarity recommender system. With input {}'
    
            '''
            return 'This is a Cosine Similarity recommender system. With input {}'.format(self.getUserInput())    
            
        #getters and setters:
        #returns the restaurant list.
        def getRestaurants(self):
            
            ''' 
            Returns the restaurants list
            
            Returns
            ------
            returns restaurant list
            '''
            return self.__restaurants
        
        #returns the user preference
        def getUserInput(self):
            ''' 
            Returns the user preference
            
            Returns
            ------
            user preference
            '''
            return self.__user_preference
        
        #returns the user preference.
        def getPreparedList(self):     
            '''
            Returns the user preference
            
            Returns
            ------
            user preference
            '''
            return self.__prepared_list
     
        #returns the the restaurant features.
        def getRestaurantFeatures(self):
            '''
            Returns the restaurant features
            
            Returns
            -------
            features:
                name of restaurant and its features
            '''
            features=self.getRestaurants().restaurantFeatures()
            return features
         
        #Sets a list with the user preferences and the restaurant features
        def setPreparedList(self):
            '''
            Sets a list with the user preferences and the restaurant features
    
            Parameters
            -------
            preparedList : function
                creates a list of restaurant features ****
                
            '''
            preparedList=self.getRestaurantFeatures()
            preparedList.append(self.getUserInput())
            preparedList.reverse()
            self.__prepared_list=preparedList
    
        #Uses cosine similarity to get the 10 more similar restaurants to the user input
        def get_similar_restaurants(self):
            '''
            Uses cosine similarity to get the 10 more similar restaurants to the user input
    
            Returns
            -------
            sorted_scores: list
                Have a list of 10 restaurants similars to user input
    
            '''
            cm=CountVectorizer().fit_transform(self.getPreparedList())
            cs=cosine_similarity(cm)
            scores=list(enumerate(cs[0]))
            sorted_scores=sorted(scores, key=lambda x:x[1], reverse=True)
            return sorted_scores[0:11]
        
        #Gets the indexes from the chosen restaurants on a list. 
        def getSelectedIndexes(self):
            '''
            Returns the indexes from the chosen restaurants on a list
    
            Returns
            -------
            indexes : list
                list the indexes of chosen restaurants
    
            '''
            indexes=[]
            for i in range(0,11):
               sorted_scores=self.get_similar_restaurants()
               selected_index=sorted_scores[i][0]
               indexes.append(selected_index)
            return indexes
            
        #Prints a list with the features of the 10 chosen restaurants. Helps to check
        #results. Probably will have to erase it later. 
        def list_results(self):
            '''
            Prints a list with the features of the 10 chosen restaurants. Helps to check
    
            Parameters
            -------
            results
                have the results of restaurants
            '''
            results=[]
            for index in self.getSelectedIndexes():
               selected=self.getPreparedList()[index]
               results.append(selected)
            print(results)
        
        #Gets the selected restaurants into a list or Restaurants
        def getSelectedRestaurants(self):
            '''
            Gets the selected restaurants into a list or Restaurants
    
            Returns
            -------
            closest : list
                list of the restaurants with features similar to user input
                
            '''
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
            '''
            
    
            Returns
            -------
            Sorted_restaurants: list
                Returns the first 3 restaurants according to the rating
            '''
            rest_list=self.getSelectedRestaurants()
            sorted_rest = sorted(rest_list, key=lambda x: x.getRating(), reverse=True)
            return sorted_rest[0:3]
            
        #Displays the 3 selected restaurants using the displayRestaurant() method from the restaurantClass.
        def outputResult(self):
            '''
            Displays the 3 selected restaurants on a dictionary name: features.
    
            Returns
            -------
            features : dictionary
                dictionary with the name of the restaurant and its features
            '''
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