# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:44:52 2021

@author: bakic
"""
#package import
import re

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
    #Prints a string when it is asked to print an instance of this class
    def __str__(self):
        return self.displayRestaurant()
    
    #method that displays the restaurant, needs a clean if it will be used for output because self.__cuisine has brackets
    def displayRestaurant(self):
        display = self.getName() + " prepares " + self.displayCuisine() + " cuisine and it's rated at " + str(self.getRating()) + " by " + str(self.getReviews()) + " people like you." 
        return display
    
    #method that returns cuisine styles from the restaurant, to be deleted later (just for checking)
    def getListedCuisine(self):
        cuisine=self.displayCuisine()
        splited=re.split(r'\W+', cuisine)
        return splited
    
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
        cuisine = self.__cuisine
            #using re package to clean the cuisine style (it is inputed as a string in the database)
        cuisine = re.sub("\'|\[|\]", "", cuisine)
        cuisine = re.sub(",", "", cuisine)
        return cuisine.lower()
    
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

if __name__=='__main__':
    restaurant = Restaurant("Hako", "['japanese', 'noodle', 'Spicy']", 1, 5, "$$ - $$$", 1000)
    restaurant.displayRestaurant()
    restaurant.getCuisine()
    restaurant.getRating()
    restaurant.getReviews()
    restaurant.displayCuisine()
    restaurant.displayPrice()
    restaurant.displayFeatures()
    print(restaurant)


    
