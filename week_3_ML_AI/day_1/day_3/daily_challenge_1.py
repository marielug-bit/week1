#==================================================
# Challenge 1: Letter Index Dictionary
# ==================================================
#
# Goal:
# Create a dictionary that stores the indices (positions)
# of each letter in a word provided by the user (input()).
#
# Key Python Topics:
# - User input (input())
# - Dictionaries
# - Loops (for loop)
# - Conditional statements (if, else)
# - String manipulation
# - Lists
#
# Instructions:
#
# 1. User Input:
#    - Ask the user to enter a word.
#    - Store the input word in a variable.
word = input('Write a word: ')
# 2. Creating the Dictionary:
#    - Iterate through each character of the input word using a loop.
#    - Check if the character is already a key in the dictionary.

def where_is_the_letter(char,word):
    ls = []
    for index,letter in enumerate(word):
        if letter == char:
            ls.append(index)
    return ls

dic = {key:where_is_the_letter(key,word) for key in set(word)}

print(dic)


#      * If it is:
#        Append the current index to the list associated with that key.
#
#      * If it is not:
#        Create a new key-value pair in the dictionary.
#
#    - Ensure that:
#        * The characters (keys) are strings.
#        * The indices (values) are stored in lists.
#
# 3. Expected Output Examples:
#
# Input: "dodo"
# Output: {"d": [0, 2], "o": [1, 3]}
#
# Input: "froggy"
# Output: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}
#
# Input: "grapes"
# Output: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}
#
# ==================================================
# Challenge 2: Affordable Items
# ==================================================
#
# Goal:
# Create a program that prints a list of items
# that can be purchased with a given amount of money.
#
# Key Python Topics:
# - Dictionaries
# - Loops (for loop)
# - Conditional statements (if, else)
# - String manipulation (replace())
# - Type conversion (int())
# - Lists
# - Sorting (sorted())
#
# Instructions:
#
# 1. Store Data:
#    - You are given a dictionary (items_purchase)
#      where:
#        * Keys = item names
#        * Values = prices as strings (with a dollar sign)
#    - The priority is defined by the order in the dictionary
#      (from most important to least important).
#    - You are also given a string (wallet)
#      representing the amount of money you have.
#
# 2. Data Cleaning:
#    - Remove the dollar sign "$"
#    - Remove commas ","
#    - Convert the cleaned string to an integer
#    - Do NOT hard-code the cleaning.
#
# 3. Determining Affordable Items:
#    - Create a list called basket.
#    - Loop through the dictionary.
#    - For each item:
#        * If you can afford it:
#            - Add the item to basket.
#            - Subtract the item price from wallet.
#
#    - If basket is empty:
#        Return the string "Nothing".
#
#    - Otherwise:
#        Print the basket list in alphabetical order.
#
# 4. Examples:
#
# Example 1:
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"
# Output: ["Bread", "Fertilizer", "Water"]
#
# Example 2:
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"
# Output: ["Apple", "Bananas", "Fan", "Honey", "Spoon"]
#
# Example 3:
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"
# Output: "Nothing"