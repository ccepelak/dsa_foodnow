
#author: @ccepelak

import pandas as pd
import numpy as np
import math
import random
import re
import geopandas as gpd
from tkinter import *

class User_Preference:
    def __init__(self, name, cuisine_style, price_range):
        self.name = name
        self.cuisine = cuisine_style
        self.price = price_range
    
    def setName(self):
        return self.name
    
    def cleanCuisineStyle(self, cuisine_style):
        self.cuisine_style = self.cuisine_style.replace(" ", ",")
        #compare inputs to restaurant list values
        for cuisine in restaurant_list:
            if self.cuisine != restaurant_list:
                print("Sorry! ", self.cuisine, " is not a valid input! Please try again.")
        return self.cuisine_style
    
    
    #def setCuisineStyle(self):
      #return self.cuisine_style
      
      
    def getCuisineStyle(self):
        return self.cuisine_style
    
    
    def getPrice(self):
        root = Tk()
  
        # Adjust size
        root.geometry( "200x200" )
    
    def show():
        label.config( text = clicked.get() )

        options = [
          "$",
          "$$",
          "$$$"]

        clicked = StringVar()

        # initial menu text
        clicked.set( "$$$" )
        
        drop = OptionMenu( root , clicked , *options )
        drop.pack()
        # Create button, it will change label text
        button = Button( root , text = "click Me" , command = show ).pack()
        # Create Label
        label = Label( root , text = " " )
        label.pack()
        # Execute tkinter
        root.mainloop()
        return self.price_range
    
    
    
    def displayFeatures(self):
        features = self.Cuisine_Style() + " " + self.getPrice()
        return features

    def outputUserFinal(self):
        return name, features 




 
  

  

 


  










