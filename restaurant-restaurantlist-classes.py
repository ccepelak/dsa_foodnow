# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:20:29 2021

@author: bakic
"""


#import required libraries

import pandas as pd
import re

#%%

#Preparing the data
df = pd.read_csv("TA_restaurants_curated.csv")

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


#%%

class Restaurant:
    
    '''
    Defines what kind of input does the restaurant take
    
    Attributes
    --------
    name:
        name of the restaurant
    cuisine:
        cuisine styles of the restaurant
    ranking:
        ranking of the restaurant
    rating:
        rating of the restaurant
    price:
        avg price of the restaurant
    reviews:
        number of reviews of the restaurant 
        
    Methods
    -------
    displayRestaurant():
        prints the restaurant
    getCuisine():
        returns cuisine styles from the restaurant
    getRating():
        return rating as a float
    getReviews():
        returns review number as an integer
    displayCuisine():
        returns cuisine styles as a string 
    displayPrice():
        displays the average price of the restaurant
    displayFeatures():
        display features of the restaurant
    getNames():
        get names of the attributes
        
    '''
    #defines what kind of input does the restaurant take
    #we can probably delete ranking, we are not using it?
    def __init__(self, name, cuisine, ranking, rating, price, reviews):
        self.__name = name
        self.__cuisine = cuisine
        self.__ranking = ranking
        self.__rating = rating
        self.__price = price
        self.__reviews = reviews
        #location to be added if there's enough time
    
    #method that displays the restaurant, needs a clean if it will be used for output because self.__cuisine has brackets
    def displayRestaurant(self):
        '''
        prints the restaurant
        
        '''
        print(f"The restaurant name is {self.__name} and it boasts {self.__cuisine} cuisine")
    
    #method that returns cuisine styles from the restaurant, to be deleted later (just for checking)
    def getCuisine(self):
        '''
        returns cuisine styles from the restaurant

        Returns
        -------
        cuisine: 
            are cuisine styles from the restaruant
        '''
        return self.__cuisine
    
    #method that returns rating as a float to be used by the RecommenderSystem class
    def getRating(self):
        '''
        returns rating as a float

        Returns
        -------
        rating : float
            floats the rating of the restaurant

        '''
        rating = float(self.__rating)
        return rating
    
    #method that returns review number as an integer to be used by the RecommenderSystem class
    def getReviews(self):
        '''
        returns review number as an integer

        Returns
        -------
        reviews : int
            returns review number as integer
        '''
        reviews = int(self.__reviews)
        return reviews        
    
    #method that cleans cuisine style (in the TripAdvisor database) and returns it as a string to be ready for the Recommender class
    def displayCuisine(self):
        '''
        returns cuisine styles as a string 

        Returns
        -------
        cuisine_string : str
            have the cuisine style of the restaurant
        '''
        cuisine_string = ""
        for i in range(len(self.__cuisine)):
            cuisine = self.__cuisine[i]
            #using re package to clean the cuisine style (it is inputed as a string in the database)
            cuisine = re.sub("\'|\[|\]", "", cuisine)
            cuisine = re.sub(",", "", cuisine)
            cuisine_string += cuisine
        return cuisine_string
    
    #method that cleans and prepares the price for the recommender system. @Angela, take a look if you want to use these categories or sth else    
    #I think I got all price tags, I've checked with df_berlin["Price_Range"].unique()
    def displayPrice(self):
        '''
        return the average price of the restaurant depending its price

        Returns
        -------
        price_string : str
            displays the average price of the restaurant

        '''
        price_string = ""
        if self.__price == "$":
            price_string = "budget"
        elif self.__price == "$$ - $$$":
            price_string = 'medium'
        else:
            price_string = 'luxury'
        return price_string
    
    #method that pastes cuisine style and price in a string so that it can be used by the RestaurantList class (and to be ready for the recommender system)
    def displayFeatures(self):
        '''
        pastes cuisine style and price in a string

        Returns
        -------
        features : function
            returns cuisine and price

        '''
        features = self.displayCuisine() + " " + self.displayPrice()
        return features

    #Getter for the name attribute
    def getName(self):
        '''
        Getter for attributes

        Returns
        -------
        name
            return the name of any attribute

        '''
        return self.__name

#%%

#just some simple tests, to be deleted later

restaurant = Restaurant("Hako", "['japanese', 'noodle']", 1, 5, "$$ - $$$", 1000)
restaurant1 = Restaurant("Hako", "['japanese', 'noodle']", 1, 5, "$", 1000)
restaurant2 = Restaurant("Hako", "['japanese', 'noodle']", 1, 5, "$$$$", 1000)

restaurant.displayRestaurant()
restaurant.getCuisine()
restaurant.getRating()
restaurant.getReviews()
restaurant.displayCuisine()
restaurant.displayPrice()

restaurant.displayFeatures()
restaurant1.displayFeatures()
restaurant2.displayFeatures()

#%%
        
class RestaurantList:
    '''
    '''
    
    def __init__(self):
        '''
        The constructor of the RestaurantList class

        Parameters
        -------
        restaurant_list:list
            list of restaurants with all attributes
            

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
    
    #creating a list of features for the recommender system from the list of restaurants using the displayFeatures 
    #method from the Restaurant class
    def restaurantFeatures(self):
        '''
        returns a list of features of the restaurants

        Returns
        -------
        features_list : list
            list of attributes of the restaurant

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
        check if the class is working

        '''
        for i in self.__restaurant_list:
            i.displayRestaurant()
            
    #Displays the list of restaurants
    def getRestaurantList(self):
        '''
        returns the restaurant list
        
        Returns
        ------
        rest_list: list
            restaurant with attributes
        '''
        rest_list=self.__restaurant_list
        return rest_list

         
#%%

#testing the restaurant class, to be deleted later

restaurants = RestaurantList()

restaurants.restaurantShow()

restaurants.restaurantFeatures()
            
