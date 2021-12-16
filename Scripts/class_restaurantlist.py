# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:07:49 2021

@author: bakic
"""
#package import
from data import df_berlin
from class_restaurant import Restaurant


class RestaurantList:
    def __init__(self):
                
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
        return 'This is a list of restaurant with {} entries'.format(len(self.getRestaurantList()))
     
    #creating a list of features for the recommender system from the list of restaurants using the displayFeatures 
    #method from the Restaurant class
    def restaurantFeatures(self):
        features_list = []
        for i in range(len(self.__restaurant_list)):
            features = self.__restaurant_list[i].displayFeatures()
            features_list.append(features)
        return features_list
    
    #just to check if the class is working, probably to delete later. displays the restaurant list using the displayRestaurant 
    #method from the Restaurant class                    
    def restaurantShow(self):
        for i in self.__restaurant_list:
            i.displayRestaurant()
            
    #Displays the list of restaurants
    def getRestaurantList(self):
        return self.__restaurant_list
    
    def getCuisineListed(self):
        cuisine_list=[]
        for  i in range(len(self.__restaurant_list)): 
            for cuisine in  self.__restaurant_list[i].getListedCuisine():
                if cuisine not in cuisine_list:
                    cuisine_list.append(cuisine)
        return cuisine_list
       
    def getSize(self):
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