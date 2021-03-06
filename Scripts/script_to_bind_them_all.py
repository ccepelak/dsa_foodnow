# -*- coding: utf-8 -*-
"""
@author: angeladuarte, ccpelak, bakic, egracialeon

This script runs the recommendation system for the app foodnow.

The script requieres  the RecommenderSystem from the class_recomender.

"""

#package import

from class_recommender import RecommenderSystem
from class_user import UserPreference

#to get recommendations, run this:

print(input(
"""
Welcome to FoodNow!
FoodNow aims to give you the best food experience in Berlin
based on what you feel like eating and how much you are willing to spend.
Of course, we only recommend the best of the best, based on reviews of people like you.
Press any key to start.
"""))

tries = 1
while tries <= 5:
    
    #creating user
    
    user=UserPreference.from_input()
    user.validateCuisineStyle()
    user.validatePrice()
    
    print("\n")
    print(user.getName() + ", you are looking for: " + user.getCuisineStyle() + " " + str(user.setPrice()) + " priced cuisine")
    print("\n")

    #minimum code to get output
    recommendation = RecommenderSystem(user.displayFeatures())
    recommendation.setPreparedList()
    recommendation.outputResult()

    happy = input("Are you happy with your recommendation? \nEnter Y for yes and N for no. ").upper()

    if happy == "Y":
        print("Thank you for using FoodNow. Enjoy!")
        break
    else:
        do_over = input("Do you want to try again? \nEnter Y for yes and N for no. ").upper()
        if do_over == "N":
            print("We are sorry you couldn't find what you were looking for.")
            break
        else:
            tries += 1
            continue
else:
    print("If we couldn't make you happy in 5 tries, we never will. Try Google maybe?")
