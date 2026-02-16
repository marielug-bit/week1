# 🌟 Exercise 1: Favorite Numbers
# ---------------------------------
# Key Python Topics:
# - Sets
# - Adding/removing items in a set
# - Set concatenation (using union)

# Instructions:
# 1. Create a set called my_fav_numbers and populate it with your favorite numbers.
# 2. Add two new numbers to the set.
# 3. Remove the last number you added to the set.
# 4. Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# 5. Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {1,2,4,5,6,8,9}
#my_fav_numbers.add(22)
#my_fav_numbers.add(26)
my_fav_numbers.update({22,26})
my_fav_numbers.remove(26)
friend_fav_numbers = {12,13,14,15}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) 



# 🌟 Exercise 2: Tuple
# ---------------------------------
# Key Python Topics:
# - Tuples (immutability)

# Instructions:
# 1. Given a tuple of integers, try to add more integers to the tuple.
# 2. Think about why you can’t add more integers to a tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation.

#tup = (1,2,3)
#tup.add(4) no add function

# 🌟 Exercise 3: List Manipulation
# ---------------------------------
# Key Python Topics:
# - Lists
# - List methods: append, remove, insert, count, clear

# Instructions:
# You have a list:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove "Banana" from the list.
basket.remove("Banana")
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
# 3. Add "Kiwi" to the end of the list.
basket.append("Kiwi")
# 4. Add "Apples" to the beginning of the list.
basket.insert(0,"Apples")
# 5. Count how many times "Apples" appear in the list.
basket.count("Apples")
# 6. Empty the list.
basket.clear()
# 7. Print the final state of the list.
print(basket)


# 🌟 Exercise 4: Floats
# ---------------------------------
# Key Python Topics:
# - Lists
# - Floats and integers
# - Range generation

# Instructions:
# 1. Recap: What is a float? What’s the difference between a float and an integer? a float is number with numbers after the comma, integer are natural numbers
# 2. Create a list containing the following sequence:
#    1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# 3. Avoid hard-coding each number manually.
# 4. Think: Can you generate this sequence using a loop or another method?
seq = "1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5"
lst = seq.split()
print(lst)


# 🌟 Exercise 5: For Loop
# ---------------------------------
# Key Python Topics:
# - Loops (for)
# - Range and indexing

# Instructions:
# 1. Write a for loop to print all numbers from 1 to 20, inclusive.
# 2. Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range(1,21):
    print(i)

for i in range(2,21,2):
    print(i)


# 🌟 Exercise 6: While Loop
# ---------------------------------
# Key Python Topics:
# - Loops (while)
# - Conditionals

# Instructions:
# 1. Use input() to ask the user to enter their name.
# 2. Using a while True loop, check if the user gave a proper name:
#    - Not digits
#    - At least 3 letters long
# 3. Hint: use the method isdigit()
# 4. If the input is incorrect, keep asking for the correct input.
# 5. If the input is correct, print “thank you” and break the loop.

counter = 1

while counter:
    name = input('what is your name?')
    has_digit = False

    for i in name:
        if i.isdigit():
            has_digit = True
            break

    if has_digit or len(name) < 3:
        print('Wrong name')
    else:
        counter = 0

print("thank you")




# 🌟 Exercise 7: Favorite Fruits
# ---------------------------------
# Key Python Topics:
# - Input/output
# - Strings and lists
# - Conditionals

# Instructions:
# 1. Ask the user to input their favorite fruits (separated by spaces).
# 2. Store these fruits in a list.
# 3. Ask the user to input the name of any fruit.
# 4. If the fruit is in their list, print:
#    "You chose one of your favorite fruits! Enjoy!"
# 5. Otherwise print:
#    "You chose a new fruit. I hope you enjoy it!"

fav_fruits = input('What are you favorite fruits?')
lst = fav_fruits.split()
fruit = input('input the name of any fruit.')
if fruit in lst:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print("You chose a new fruit. I hope you enjoy it!")

# 🌟 Exercise 8: Pizza Toppings
# ---------------------------------
# Key Python Topics:
# - Loops
# - Lists
# - String formatting

# Instructions:
# 1. Write a loop that asks the user to enter pizza toppings one by one.
# 2. Stop the loop when the user types 'quit'.
# 3. For each topping entered, print:
#    "Adding [topping] to your pizza."
# 4. After exiting the loop:
#    - Print all the toppings.
#    - Calculate the total cost.
# 5. The base price is $10.
# 6. Each topping adds $2.50.

counter = 1
lst = []
while counter:
    top = input('What topping do you want on your pizza?')
    if top != 'quit':
        print(f'Adding {top} to your pizza.')
        lst.append(top)
    else:
        counter = 0
cost = 10 + 2.50*len(lst)
print(f"Your toppings are {', '.join(lst)} and the cost is {cost} $" )



    

# 🌟 Exercise 9: Cinemax Tickets
# ---------------------------------
# Key Python Topics:
# - Conditionals
# - Lists
# - Loops

# Instructions:
# 1. Ask for the age of each person in a family who wants to buy a movie ticket.
# 2. Calculate the total cost:
#    - Free for under 3
#    - $10 for ages 3–12
#    - $15 for over 12
# 3. Print the total ticket cost.
ages = input('What are the ages of your family?')
ages_lst = ages.split()
cost = 0
for i in ages_lst :
    i = int(i)
    if 3 <= i <= 12:
        cost +=10
    if i > 12:
        cost +=15
print(f'the total cost is {cost}')


# Bonus:
# Imagine a restricted movie (only ages 16–21).
# 1. Ask for each person’s age.
# 2. Remove anyone who isn’t allowed.
# 3. Print the final list of attendees.
dct = {}

while True:
    name = input("What is your name? If everyone has already told his name, write 'quit': ")
    if name == "quit":
        break
    age = int(input("How old are you? "))
    dct[name] = age

lst = []
for key, value in dct.items():
    if 16 <= value <= 21:
        lst.append(key)

for person in lst:
    print(person)



