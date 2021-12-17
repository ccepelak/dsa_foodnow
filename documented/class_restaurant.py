# -*- coding: utf-8 -*-
"""
@author: angeladuarte, ccpelak, bakic, egracialeon

This script creates a class Restaurant with all the features that will be used 
in the recommender class. 

The script requieres  "re"

This file can also be imported as a module and contains the following
functions:
    
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
        
    
  
"""
#package import
import re

class Restaurant:
    '''
    A class used to represent the Restaurant
    
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
    getName():
        get names of the attributes
        
    '''
    #defines what kind of input does the restaurant take
    #we can probably delete ranking, we are not using it?
    def __init__(self, name, cuisine, ranking, rating, price, reviews):
        '''
        This is the constructor of the Restaurant class

        Parameters
        ----------
        name : str
            name of the restaurant
        cuisine : str
            type of cuisine they offer(features)
        ranking : int
            ranking of the restaurant
        rating : int
            rating of the restaurant
        price : str
            average price
        reviews : int
            number of reviews

        Returns
        -------
        None.

        '''
        self.__name = name
        self.__cuisine = cuisine
        self.__ranking = ranking
        self.__rating = rating
        self.__price = price
        self.__reviews = reviews
        #location to be added if there's enough time
    #Prints a string when it is asked to print an instance of this class
    def __str__(self):
        '''
        prints the name of the restaurant and its features
        
        Returns
        -------
        displayRestaurant()
            Shows the restaurant and all the information

        '''
        return self.displayRestaurant()
    
    #method that displays the restaurant, needs a clean if it will be used for output because self.__cuisine has brackets
    def displayRestaurant(self):
        '''
        displays the restaurant 

        Returns
        -------
        display : str
            a string with all features of the restaurant and more information

        '''
        display = self.getName() + " prepares " + self.displayCuisine() + " cuisine and it's rated at " + str(self.getRating()) + " by " + str(self.getReviews()) + " people like you." 
        return display
    
    #method that returns cuisine styles from the restaurant, to be deleted later (just for checking)
    def getListedCuisine(self):
        '''
        returns cuisine styles from the restaurant

        Returns
        -------
        cuisine: 
            are cuisine styles from the restaruant
        '''
        cuisine=self.displayCuisine()
        splited=re.split(r'\W+', cuisine)
        return splited
    
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
        cuisine = self.__cuisine
            #using re package to clean the cuisine style (it is inputed as a string in the database)
        cuisine = re.sub("\'|\[|\]", "", cuisine)
        cuisine = re.sub(",", "", cuisine)
        return cuisine.lower()
    
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


    
