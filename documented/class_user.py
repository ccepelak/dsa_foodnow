#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

@author: angeladuarte

This script allows the user to input his/her restaurant preferences to the
recommender system. 

This program accepts input as a string/list

The script requieres "re", "tkinter", and "class_restaurantlist" be installed
within the Python environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * 
'''

import re
from tkinter import *
from class_restaurantlist import RestaurantList


class User_Preference:
    '''
    A class used to represent the user preferences
    '''
    
    def __init__(self, name, cuisine_style):
        '''
        This is the constructor of the class Recomender System

        Parameters
        ----------
        name : str
            name of the user
        cuisine_style : list
            preferences of the user

        Returns
        -------
        None.

        '''
        
        self.name = name
        self.cuisine_style = cuisine_style
        self.price=""
        
    @classmethod
    def from_input(cls):
        '''
        

        This is a class 
        ----------
        cls : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return cls(input("What is your name? "), 
                   input("""What would you like to eat? Add cuisine descriptions like vegan, gluten-free, or japanese.
                 Make sure to separate your entries with a comma (,). """))

    
    def getName(self):
        '''
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return self.name
    
    def setPrice(self):
        '''
        

        Returns
        -------
        None.

        '''
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
        '''
        get the user price preference

        Returns
        -------
        price: 
            

        '''
        return self.price
        
    def setCuisineStyle(self):
        '''
        sets the cuisine style preference of the user

        Returns
        -------
        None.

        '''
        pass
    
    def cleanCuisineStyle(self):
        '''
        cleans the cuisine style preference input from the user

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        cuisine=self.cuisine_style
        cuisine = re.sub("\'|\[|\]", "", cuisine)
        cuisine = re.sub(",", "", cuisine)
        return cuisine.lower()
    
    def validateCuisineStyle(self):
        '''
        

        Returns
        -------
        None.

        '''
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
