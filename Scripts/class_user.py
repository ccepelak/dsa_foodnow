#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:23:30 2021

@author: angeladuarte and @ccepelak
"""

import re
from tkinter import *
from class_restaurantlist import RestaurantList


class User_Preference:
    
    def __init__(self, name, cuisine_style):
        self.name = name
        self.cuisine_style = cuisine_style
        self.price=""
        
    @classmethod
    def from_input(cls):
        return cls(input("What is your name? "), 
                   input("""What would you like to eat? Add cuisine descriptions like vegan, gluten-free, or japanese.
                 Make sure to separate your entries with a comma (,). """))

    
    def getName(self):
        return self.name
    
    def setPrice(self):
        root = Tk()
        OPTIONS = ["budget", "medium", "luxury"] 
        variable = StringVar(root)
        variable.set(OPTIONS[0]) # default value
        w = OptionMenu(root, variable, *OPTIONS)
        root.geometry( "200x200" )
        w.pack()
        def ok():
            print ("value is:" + variable.get())
        button = Button(root, text="OK", command=ok)
        button.pack()
        mainloop()
        self.price=variable.get() 
        
    def getPrice(self):
        return self.price
        
    def setCuisineStyle(self):
        pass
    
    def cleanCuisineStyle(self):
        cuisine=self.cuisine_style
        cuisine = re.sub("\'|\[|\]", "", cuisine)
        cuisine = re.sub(",", "", cuisine)
        return cuisine.lower()
    
    def validateCuisineStyle(self):
        restaurantList=RestaurantList()
        cuisines=restaurantList.getCuisineListed()
        preferred_cuisine=re.split(r'\W+', self.cuisine_style.lower())
        #compare inputs to restaurant list values
        for i in range(len(preferred_cuisine)):
            if preferred_cuisine[i] not in cuisines:
              print("Sorry! ", preferred_cuisine[i], " is not a valid input! Please try again.")
              new_cuisine=input("""What would you like to eat? Add cuisine descriptions like halal, gluten-free, or japanese.
            Make sure to separate your entries with a comma (,). """)
              self.cuisine_style=new_cuisine
            else:
                break
      
    def getCuisineStyle(self):
        return self.cuisine_style
    
    def displayFeatures(self):
        features = self.cleanCuisineStyle() + " " + self.getPrice()
        return features

    def outputUserFinal(self):
        return self.getName(), self.displayFeatures() 



#%%

if __name__=='__main__':
    user1=User_Preference.from_input()
    user1.getName()
    user1.getCuisineStyle()
    user1.cleanCuisineStyle()
    user1.validateCuisineStyle()
    user1.setPrice()
    user1.getPrice()
    user1.displayFeatures()
    user1.outputUserFinal()

#%%
