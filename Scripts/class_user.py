#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:23:30 2021

@author: angeladuarte and @ccepelak
"""

import re
from tkinter import *
from class_restaurantlist import RestaurantList


class UserPreference:
    #Constructor
    def __init__(self, name, cuisine_style, price):
        self.name = name
        self.cuisine_style = cuisine_style
        self.price=price
        
    @classmethod
    def from_input(cls):
        return cls(input("What is your name? "), 
                   input("""What would you like to eat? Add cuisine descriptions like vegan, gluten-free, or japanese.
                 Make sure to separate your entries with a comma (,). """),
                 input("""What is your preferred price?
                       Enter 1 for budget; 2 for medium; and 3 for luxury:
                       """))
 
    def getName(self):
        return self.name
    
    def getPrice(self):
        return int(self.price)
    
    def validatePrice(self):
        price=int(self.getPrice())
        while price not in range(1, 3, 1):
            print("Sorry! We don't understant what you meant with the price:" + str(self.getPrice()))
            price=int(input("Please enter 1 for budget; 2 for medium; and 3 for luxury."))
        self.price=price
    
    def setPrice(self):
        price_string=""
        if self.price == 1:
            price_string = "budget"
        elif self.price == 2:
            price_string = 'medium'
        else:
            price_string = 'luxury'
        return price_string
        
    def setCuisineStyle(self):
        self.cuisine_style=cleanCuisineStyle()
    
    def cleanCuisineStyle(self):
        cuisine=self.cuisine_style
        cuisine = re.sub("\'|\[|\]", "", cuisine)
        cuisine = re.sub(",", "", cuisine)
        return cuisine.lower()
    
    def validateCuisineStyle(self):
        restaurantList=RestaurantList()
        cuisines=restaurantList.getCuisineListed()
        preferred_cuisine=re.split(r'\W+', self.cuisine_style.lower())
        print(preferred_cuisine)
        #compare inputs to restaurant list values
        for i in range(len(preferred_cuisine)):
            if preferred_cuisine[i] not in cuisines:
                print("Sorry! ", preferred_cuisine[i], " is not a valid input! Please try again.")
                new_cuisine=input("""What would you like to eat? Add cuisine descriptions like halal, gluten-free, or japanese.
              Make sure to separate your entries with a comma (,). """)
                self.cuisine_style=new_cuisine
                
    def getCuisineStyle(self):
        return self.cuisine_style
    
    def displayFeatures(self):
        features = self.cleanCuisineStyle() + " " + self.setPrice()
        return features

    def outputUserFinal(self):
        return self.getName(), self.displayFeatures() 



#%%

if __name__=='__main__':
    user1=UserPreference.from_input()
    user1.getName()
    user1.getCuisineStyle()
    user1.validateCuisineStyle()
    user1.cleanCuisineStyle()
    user1.validatePrice()
    user1.setPrice()
    user1.getPrice()
    user1.displayFeatures()
    user1.outputUserFinal()
    

#%%

restaurantList=RestaurantList()
cuisines=restaurantList.getCuisineListed()
preferred_cuisine=re.split(r'\W+', "japanese, glass")
print(preferred_cuisine)
     #compare inputs to restaurant list values
     for i in range(len(preferred_cuisine)):
         if preferred_cuisine[i] not in cuisines:
             print("Sorry! ", preferred_cuisine[i], " is not a valid input! Please try again.")
             new_cuisine=input("""What would you like to eat? Add cuisine descriptions like halal, gluten-free, or japanese.
           Make sure to separate your entries with a comma (,). """)
             self.cuisine_style=new_cuisine
             