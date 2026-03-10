# ==================================================
# Exercise 1 : Geometry
# ==================================================
# Instructions:
# Write a class called Circle that receives a radius as an argument.
# The default value of the radius should be 1.0.
#
# Write two instance methods:
# - One method to compute the perimeter of the circle.
# - One method to compute the area of the circle.
#
# Write a method that prints the geometrical definition of a circle.
import math
class Circle:
    def __init__(self,radius = 1.0):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius**2)
    
    def definition(self):
        print("A circle is the set of all points in a plane " \
        "that are at a fixed distance (radius) from a central point.")
# ==================================================
# Exercise 2 : Custom List Class
# ==================================================
# Instructions:
# Create a class called MyList.
# The class should receive a list of letters.
#
# Add a method that returns the reversed list.
#
# Add a method that returns the sorted list.
#
# Bonus:
# Create a method that generates a second list
# with the same length as mylist.
# The list should be constructed with random numbers.
# (Use list comprehension.)
import random

class MyList:
    def __init__(self,letters : list):
        self.letters = letters

    def reverse_letters(self):
        return self.letters[::-1]
    
    def sorted_letters(self):
        return sorted(self.letters)
    
    def another_list(self):
        return [random.random() for i in range(len(self.letters))]
# ==================================================
# Exercise 3 : Restaurant Menu Manager
# ==================================================
# Instructions:
# The purpose of this exercise is to create a restaurant menu.
# The code will allow a manager to add and delete dishes.
#
# Create a python file called menu_manager.py.
#
# Create a class called MenuManager.
#
# Create a method __init__ that instantiates an attribute
# called menu.
#
# The menu attribute value will be all the current dishes
# (a list of dictionaries).
#
# Each dish will be stored in a dictionary where the keys are:
# - name
# - price
# - spice level
# - gluten index (boolean value)
#
# Here is the list of dishes currently on the menu:
#
# Soup – 10 – B - False
# Hamburger – 15 - A - True
# Salad – 18 - A - False
# French Fries – 5 - C - False
# Beef bourguignon – 25 - B - True
#
# Meaning for spice level:
# A = not spicy
# B = a little spicy
# C = very spicy
#
# The dishes provided above should be the value
# of the menu attribute.
#
# Create a method called add_item(name, price, spice, gluten).
# This method will add new dishes to the menu.
#
# Create a method called update_item(name, price, spice, gluten).
# This method checks whether a dish is in the menu.
# If the dish exists, update it.
# If not, notify the manager that the dish is not in the menu.
#
# Create a method called remove_item(name).
# This method should check if the dish is in the menu.
# If the dish exists, delete it and print the updated dictionary.
# If not, notify the manager that the dish is not in the menu.