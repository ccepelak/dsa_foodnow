# -*- coding: utf-8 -*-
"""
@author: angeladuarte, ccpelak, bakic, egracialeon

This script runs the recommendation system for the app foodnow.

The script requieres  the RecommenderSystem from the class_recomender.

"""

#package import

from class_recommender import RecommenderSystem

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
