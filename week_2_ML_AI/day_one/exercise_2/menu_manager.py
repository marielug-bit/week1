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
class MenuManager:
    def __init__(self,menu : list):
        self.menu = menu
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

    def add_item(self,name, price, spice, gluten):
        self.menu.append({'name':name, 'price': price, 'spice level':spice, 
                          'gluten index':gluten})
        
# Create a method called update_item(name, price, spice, gluten).
# This method checks whether a dish is in the menu.

    def update_item(self,name, price, spice, gluten):
        for index, dic in self.menu.enumerate():
            if dic['name'] == name:
                self.menu [index] = {'name':name, 'price': price, 'spice level':spice, 
                          'gluten index':gluten}
                return
            
        print('there is no such dish in the menu.')
                
# If the dish exists, update it.
# If not, notify the manager that the dish is not in the menu.

    def remove_item(self,name):
        for index, dic in enumerate(self.menu):
            if dic['name'] == name:
                self.menu.remove(self.menu[index])
                return
        print('there is no such dish in the menu.')
# Create a method called remove_item(name).
# This method should check if the dish is in the menu.
# If the dish exists, delete it and print the updated dictionary.
# If not, notify the manager that the dish is not in the menu.