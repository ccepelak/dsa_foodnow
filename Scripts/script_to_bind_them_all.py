# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:08:10 2021

@author: bakic
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
    
    #user
    
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

    happy = input("Are you happy with your recommendation, " + user.getName() + "?" + "\nEnter Y for yes and N for no.").upper()

    if happy == "Y":
        print(user.getName() + ", thank you for using FoodNow. Enjoy!")
        break
    else:
        do_over = input("Do you want to try again? \nEnter Y for yes and N for no. ").upper()
        if do_over == "N":
            print("We are sorry you couldn't find what you were looking for, " + user.getName())
            break
        else:
            tries += 1
            continue
else:
    print("If we couldn't make you happy in 5 tries, we never will. Try Google maybe?")





tries = 1
while tries <= 5:
    
    cuisine = input("""What would you like to eat? Add cuisine descriptions like halal, gluten-free, or japanese.
             Make sure to separate your entries with a comma (,).""")
    price = input("""What is your prefered price range? /n
              Enter 'budget', 'medium' or 'luxury' """)

    #to be deleted with user class
    user = cuisine + " " + price

    print("You are looking for: " + user)

    #minimum code to get output
    recommendation = RecommenderSystem(user)
    recommendation.setPreparedList()
    recommendation.outputResult2()

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
