# -*- coding: utf-8 -*-
"""
@author: angeladuarte, ccpelak, bakic, egracialeon

This script creates a list of all features of the restaurant  that will be used 
in the recommender class. 

The script requieres  the database df_berlin and the Restaurant from the
class_restaurant.

This file can also be imported as a module and contains the following
functions:
    restaurantFeatures():
        create a list of features for the recommender system from the restaurants
    restaurantShow():
        shows the restaurant 
    getRestaurantList():
        displays the list of restaurants
    getCuisineListed():
        lists the type of cuisine of the restaurants
    getSize():
        get the lenght of the features of the restaurants

    
    
    
"""
#package import
from data import df_berlin
from class_restaurant import Restaurant


class RestaurantList:
    '''
    A class used to represent all the features of the restaurant in RestaurantList
    
    Attributes: 
    --------
    restaurant_list:
        list of features of the restaurants as name, ranking reviews, rating...
    
    Methods:
    -------
    restaurantFeatures():
        create a list of features for the recommender system from the restaurants
    restaurantShow():
        shows the restaurant 
    getRestaurantList():
        displays the list of restaurants
    getCuisineListed():
        lists the type of cuisine of the restaurants
    getSize():
        get the lenght of the features of the restaurants
    
    '''
    def __init__(self):
        '''
        This is the constructor of the class RestaurantList

        Returns
        -------
        None.

        '''
                
        #creates empty list
        self.__restaurant_list = []  
        
        #here iterrate over data frame using pandas to create a restaurant list. Take note that the column names have been changed
        #to not include empty spaces, I didn't manage otherwise. If we can find a way to iterrate over rows with original names, that might be better
        for index, rows in df_berlin.iterrows():
            #create list from current row using Restaurant class
            restaurant = Restaurant(rows.Name, rows.Cuisine_Style, rows.Ranking, rows.Rating, rows.Price_Range, rows.Number_of_Reviews)
            #append the list
            self.__restaurant_list.append(restaurant)
    #Prints a string when it is asked to print an instance of this class   
    def __str__(self):
        '''
        prints a string when it is asked to print an instance of this class

        Returns
        -------
        str
         a string with a list of restaurants

        '''
        return 'This is a list of restaurant with {} entries'.format(len(self.getRestaurantList()))
     
    #creating a list of features for the recommender system from the list of restaurants using the displayFeatures 
    #method from the Restaurant class
    def restaurantFeatures(self):
        '''
        create a list of features for the recommender system from the restaurants

        Returns
        -------
        features_list : list
            list with features of restaurants

        '''
        features_list = []
        for i in range(len(self.__restaurant_list)):
            features = self.__restaurant_list[i].displayFeatures()
            features_list.append(features)
        return features_list
    
    #just to check if the class is working, probably to delete later. displays the restaurant list using the displayRestaurant 
    #method from the Restaurant class                    
    def restaurantShow(self):
        '''
        shows the restaurant 

        Returns
        -------
        None.

        '''
        for i in self.__restaurant_list:
            i.displayRestaurant()
            
    #Displays the list of restaurants
    def getRestaurantList(self):
        '''
        displays the list of restaurants

        Returns
        -------
        list 
            features of the restaurant

        '''
        return self.__restaurant_list
    
    def getCuisineListed(self):
        '''
        lists the type of cuisine of the restaurants

        Returns
        -------
        cuisine_list : list
            features of the restaurant

        '''
        cuisine_list=[]
        for  i in range(len(self.__restaurant_list)): 
            for cuisine in  self.__restaurant_list[i].getListedCuisine():
                if cuisine not in cuisine_list:
                    cuisine_list.append(cuisine)
        return cuisine_list
       
    def getSize(self):
        '''
        get the lenght of the features of the restaurants

        Returns
        -------
        length : TYPE
            number of features in the restaurant

        '''
        length=len(self.__restaurant_list)
        return length

#%%
 #testing the restaurant class, to be deleted later
if __name__=='__main__':
    restaurants = RestaurantList()
    restaurants.restaurantShow()
    restaurants.restaurantFeatures()
    print(restaurants)
    print(restaurants.getRestaurantList())