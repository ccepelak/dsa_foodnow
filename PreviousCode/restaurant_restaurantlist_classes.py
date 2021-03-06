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
        display = self.getName() + " prepares " + self.displayCuisine() + " cuisine and it's rated at " + str(self.getRating()) + " by " + str(self.getReviews()) + " people like you." 
        return display
    
    #method that returns cuisine styles from the restaurant, to be deleted later (just for checking)
    def getCuisine(self):
        return self.__cuisine
    
    #method that returns rating as a float to be used by the RecommenderSystem class
    def getRating(self):
        rating = float(self.__rating)
        return rating
    
    #method that returns review number as an integer to be used by the RecommenderSystem class
    def getReviews(self):
        reviews = int(self.__reviews)
        return reviews        
    
    #method that cleans cuisine style (in the TripAdvisor database) and returns it as a string to be ready for the Recommender class
    def displayCuisine(self):
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
        features = self.displayCuisine() + " " + self.displayPrice()
        return features

    #Getter for the name attribute
    def getName(self):
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
        rest_list=self.__restaurant_list
        return rest_list

         
#%%

#testing the restaurant class, to be deleted later

restaurants = RestaurantList()

restaurants.restaurantShow()

restaurants.restaurantFeatures()
            
