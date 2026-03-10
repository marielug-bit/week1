# 🌟 Exercise 1: Converting Lists into Dictionaries
# ==================================================
# Key Python Topics:
# - Creating dictionaries
# - Using the zip() function or dictionary comprehension
#
# Instructions:
# You are given two lists.
# Convert them into a dictionary where:
# - The first list contains the keys
# - The second list contains the corresponding values
#
# Lists:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = {}
for key, value in zip(keys,values):
    dic[key]=value
print(dic)

# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# 🌟 Exercise 2: Cinemax #2
# ==================================================
# Key Python Topics:
# - Looping through dictionaries
# - Using conditionals (if / elif / else)
# - Performing calculations
#
# Instructions:
# Write a program that calculates the total cost of movie tickets
# for a family based on their ages.
#
# The family members' ages are stored in a dictionary.
#
# Ticket pricing rules:
# - Under 3 years old: Free
# - 3 to 12 years old: $10
# - Over 12 years old: $15
#
# Family Data:
#family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
cost = 0
family = {}
family_input = input("input family members' names and ages Name age")
lst = family_input.split()
lst_name = [lst[index] for index in range(len(lst)) if index%2 == 0]
lst_ages = [lst[index] for index in range(len(lst)) if index%2 == 1]
for key, value in zip(lst_name,lst_ages):
    family[key]=int(value)

for key, value in family.items():
    if value > 12 :
        cost+=15
        print(f'the ticket price for {key} is 15.')
    if 3<=value<=12:
        cost+=10
        print(f'the tichet price for {key} is 10')
    if value < 3:
        print(f'the ticket price for {key} is 0')
print(f'total cost is {cost}')
#
# Tasks:
# - Loop through the family dictionary
# - Calculate the ticket price for each family member
# - Print the ticket price for each person
# - Print the total cost at the end
#
# Bonus:
# Allow the user to input family members' names and ages,
# then calculate the total ticket cost. 
#==================================================
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
# ==================================================
#
# Brand Information:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
# Tasks:
# 1. Create a dictionary called brand with the provided data.
brand = {'name':'Zara', 'creation_date':1975, 'creator_name':'Amancio Ortega Gaona', 
         'type_of_clothes': ['men', 'women', 'children', 'home'], 'international_competitors':['Gap', 'H&M', 'Benetton'],
          'number_stores':7000, 'major_color':{'France': 'blue', 'Spain': 'red', 'US': 'pink, green' }  }
# 2. Change the value of number_stores to 2.
brand['number_stores']=2
# 3. Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara sells cloths for {' '.join(brand['type_of_clothes'])}.")
# 4. Add a new key country_creation with the value Spain.
brand['country_creation'] = 'Spain'
# 5. Check if international_competitors exists and, if so, add “Desigual” to the list.
if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual') 
# 6. Delete the creation_date key.
del brand['creation_date']
# 7. Print the last item in international_competitors.
print(brand['international_competitors'][-1])
# 8. Print the major colors in the US.
print(brand['major_color']['US'])
# 9. Print the number of keys in the dictionary.
num = len(brand)
print(num)
# 10. Print all keys of the dictionary.
print(' '.join(brand.keys()))
# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores.
# Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {'creation_date':1975, 'number_stores':7000}
brand.update(more_on_zara)
print(brand)
#
# ==================================================
# 🌟 Exercise 4: Disney Characters
# Key Python Topics:
# - Looping with indexes
# - Dictionary creation
# - Sorting
# ==================================================
#
# Instructions:
# You are given a list of Disney characters. Create three dictionaries based on different patterns:
#
# Character List:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#
# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
#    {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
dic1 = {}
for index, name in enumerate(users):
    dic1[name]=index
#
# 2. Create a dictionary that maps indices to characters:
#    {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
dic2 = {}
for index, name in enumerate(users):
    dic2[index]=name

#
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#    {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

new_users = sorted(users)
dic3 = {}
for index, name in enumerate(new_users):
    dic3[name]=index

