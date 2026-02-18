# ================================================
# Exercise 1: Birthday Look-up
# ================================================
#
# Instructions:
#
# 1. Create a variable called "birthdays".
#    - It should be a dictionary.
#    - Add 5 people of your choice.
#    - Keys = person’s name
#    - Values = birthday in format "YYYY/MM/DD"
birthdays = {'Marie':'1998/12/02', 'David':'1997/04/19', 'Johanna':'1969/03/18', 'Cyril':'1968/12/25', 'Yehuda':'2025/01/12' }
# 2. Print a welcome message for the user.
#    Example:
print(birthdays)
print("Welcome! You can look up the birthdays of the people in the list!")

#
# 3. Ask the user to enter a person’s name.
#    - Store the input in a variable.
new_name = input("Enter a person's name")

# 4. Retrieve the birthday corresponding to that name.
birthday = birthdays.get(new_name)

if birthday:
    print(f"{new_name}'s birthday is {birthday}.")
else:
    print(f"Sorry, we don’t have the birthday information for {new_name}.")
#
# 5. Print the birthday using a nicely formatted message.
#    Example:
#    "Alice's birthday is 1995/04/21"


# ================================================
# Exercise 2: Birthdays Advanced
# ================================================
#
# Instructions:
#
# 1. Before asking for user input:
#    - Print all the names available in the dictionary.
#
# 2. If the user enters a name that does NOT exist:
#    - Print:
#      "Sorry, we don’t have the birthday information for <person's name>"


# ================================================
# Exercise 3: Add Your Own Birthday
# ================================================
#
# Instructions:
#
# 1. Before asking the user to look up a birthday:
#    - Ask the user to add a new birthday.
#
# 2. Ask for:
#    - Person’s name → store in a variable.
#    - Person’s birthday ("YYYY/MM/DD") → store in a variable.
user_name = input('What is your name?')
user_date = input("what is your birthday date? YYYY/MM/DD")
birthdays = {'Marie':'1998/12/02', 'David':'1997/04/19', 'Johanna':'1969/03/18', 'Cyril':'1968/12/25', 'Yehuda':'2025/01/12' }
birthdays[user_name] = user_date
print(birthdays)

# 3. Add this new data to the dictionary.
#
# 4. Make sure that:
#    - If the user searches for ANY name in the dictionary
#      (including the one they just added),
#      the birthday is found and displayed correctly.
input_name = input('Write a name: ')
input_name_in_dic = birthdays.get(input_name,0)
if input_name_in_dic:
    print(f'{input_name} s birthday is {birthdays[input_name]}')
else:
    print('there is no such name')


# ================================================
# Exercise 4: Fruit Shop
# ================================================
#
# Part 1:
#
# Given this dictionary:
#
items = {
     "banana": 4,
     "apple": 2,
     "orange": 1.5,
     "pear": 3
 }
#
# Each key = item name
# Each value = price
#
# Task:
# - Print all items and their prices in a sentence.
#   Example:
#   "The price of banana is 4"
for item,value in items.items():
    print(f'the price of {item} is {value}')

# ------------------------------------------------
# Part 2:
#
# Given this dictionary:
#
items = {
     "banana": {"price": 4, "stock": 10},
     "apple": {"price": 2, "stock": 5},
     "orange": {"price": 1.5, "stock": 24},
     "pear": {"price": 3, "stock": 1}
 }
#
# Each item now contains:
# - price
# - stock
#
# Task:
# - Calculate the total cost to buy EVERYTHING in stock.
#   (price * stock for each item)
# - Print the final total amount.

item_cost = 0
for item in items.keys():
    item_cost += items[item]['price']*items[item]['stock']
print(item_cost) 

# ================================================
# One Last Thing:
# ================================================
# Good luck! 🚀