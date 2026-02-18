# ==================================================
# Exercises XP
# ==================================================


# ==================================================
# 🌟 Exercise 1: What Are You Learning?
# Goal: Create a function that displays a message about what you’re learning.
# ==================================================
#
# Key Python Topics:
# - Functions (defining and calling)
# - print() function
#
# Step 1: Define a function named display_message()
#   - This function should not take any parameters.

# Step 2: Print a message inside the function
#   Example: "I am learning about functions in Python."
#
# Step 3: Call the function to display the message

# Expected Output:
# I am learning about functions in Python.

def display_message():
    print("I am learning about functions in Python.")

display_message()
# ==================================================
# 🌟 Exercise 2: What’s Your Favorite Book?
# Goal: Create a function that displays a message about a favorite book.
# ==================================================
#
# Key Python Topics:
# - Functions with parameters
# - String concatenation or f-strings
# - Calling functions with arguments
#
# Step 1: Define a function named favorite_book(title)
#   - It accepts one parameter: title
#
# Step 2: Print a message using the title
#   Example: "One of my favorite books is <title>"
#
# Step 3: Call favorite_book() with an argument
#   Example: favorite_book("Alice in Wonderland")

def favorite_book(title):
    print(f'One of my favorite books is {title}.')

favorite_book("Alice in Wonderland")

# ==================================================
# 🌟 Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.
# ==================================================
#
# Key Python Topics:
# - Functions with multiple parameters
# - Default parameter values
# - String formatting
#
# Step 1: Define a function named describe_city(city, country="Unknown")
#   - city is required
#   - country has a default value "Unknown"
#
# Step 2: Print a message inside the function
#   Example: "<city> is in <country>"
#
# Step 3: Call the function in different ways:
#   - describe_city("Reykjavik", "Iceland")
#   - describe_city("Paris")  # uses default country
#
# Expected Output:
# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
# ==================================================
# 🌟 Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.
# ==================================================
#
# Key Python Topics:
# - random module
# - random.randint()
# - Conditional statements (if, else)
#
# Step 1: Import random at the top of your script
#   import random
#
# Step 2: Define a function that accepts a number (1 to 100) as a parameter
#
# Step 3: Inside the function generate a random number:
#   random.randint(1, 100)
#
# Step 4: Compare user number with random number:
#   - If same: print "Success!"
#   - Else: print "Fail! Your number: X, Random number: Y"
#
# Step 5: Call the function with a number between 1 and 100
#
# Expected Output:
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)
import random
def guess_func(num):
    if not (1 <= num <= 100):
        raise ValueError ('the value should be betwen 1 and 100')
    random_num = random.randint(1,100)
    if random_num == num:
        print("Success!")
    else:
        print(f"Fail! Your number: {num}, Random number: {random_num}") 


# ==================================================
# 🌟 Exercise 5: Let’s Create Some Personalized Shirts!
# Goal: Create a function to describe a shirt’s size and message, with default values.
# ==================================================
#
# Key Python Topics:
# - Functions with parameters and default values
# - Keyword arguments
#
# Step 1: Define a function make_shirt(size, text)
#
# Step 2: Print a summary message
#   Example: "The size of the shirt is <size> and the text is <text>"
#
# Step 3: Call the function
#
# Step 4: Modify the function so it has default values:
#   - size="large"
#   - text="I love Python"
#
# Step 5: Call the function using:
#   - default values
#   - custom size with default text
#   - custom size + custom text
#
# Step 6 (Bonus): Call make_shirt() using keyword arguments:
#   make_shirt(size="small", text="Hello!")
#
# Expected Output:
# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

#def make_shirt(size, text):
#    print(f"The size of the shirt is {size} and the text is {text}.")

#make_shirt(38,'I LOVE NY')

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")
make_shirt(38)
make_shirt(text ='I LOVE NY')
make_shirt()
make_shirt(size="small", text="Hello!")

# ==================================================
# 🌟 Exercise 6: Magicians…
# Goal: Modify a list of magician names and display them in different ways.
# ==================================================
#
# Key Python Topics:
# - Lists
# - for loops
# - Modifying lists
# - Functions that modify data structures
#
# Step 1: Create a list called magician_names:
#   ['Harry Houdini', 'David Blaine', 'Criss Angel']
#
# Step 2: Create a function show_magicians(magician_names)
#   - Loop through the list
#   - Print each name
#
# Step 3: Create a function make_great(magician_names)
#   - Loop through the list
#   - Add "the Great" before each name (modify the list)
#
# Step 4: Call make_great() then call show_magicians()
#
# Expected Output:
# Harry Houdini the Great
# David Blaine the Great
# Criss Angel the Great
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)
    # print(' '.join(magician_names))

def make_great_one_name(name):
    new = name + ' the Great'
    return new

def make_great(magician_names):
    new_list = list(map(make_great_one_name, magician_names))
    print('\n'.join(new_list))

    
show_magicians(magician_names)
make_great(magician_names)
# ==================================================
# 🌟 Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
# ==================================================
#
# Key Python Topics:
# - Functions
# - Conditionals (if / elif)
# - Random numbers
# - Floating-point numbers (Bonus)
# - Handling seasons (Bonus)
#
# Step 1: Create get_random_temp()
#   - Return a random integer between -10 and 40

def get_random_temp():
    return random.randint(-10,40)

# Step 2: Create main()
#   - Call get_random_temp()
#   - Print: "The temperature right now is X degrees Celsius."

def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp} degrees Celsius.')
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    if 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    if 16 <= temp <= 23:
        print("Nice weather.")
    if 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    if 32 <= temp <= 40:
        print("It’s really hot! Stay cool.")

#
# Step 3: Provide advice based on temperature:
#   - Below 0°C:
#     "Brrr, that’s freezing! Wear some extra layers today."
#   - 0°C to 16°C:
#     "Quite chilly! Don’t forget your coat."
#   - 16°C to 23°C:
#     "Nice weather."
#   - 24°C to 32°C:
#     "A bit warm, stay hydrated."
#   - 32°C to 40°C:
#     "It’s really hot! Stay cool."
#
# Step 4 (Bonus): Use random.uniform() to return a float temperature
def get_random_temp():
    return random.uniform(-10,40)
def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp:.1f} degrees Celsius.')
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    if 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    if 16 <= temp <= 23:
        print("Nice weather.")
    if 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    if 32 <= temp <= 40:
        print("It’s really hot! Stay cool.")
#
# Step 5 (Bonus): Ask user for month (1-12) and determine season
#   - Modify get_random_temp() to return temperatures based on season
month = input('Write a month (1-12): ')
def get_random_temp():
    if month 1<= month <= 2 or month = 12 :
        return random.uniform(-10,0)
    if 3 <= month <= 5:
        return random.uniform(0,16)
    if 6 <= month <=8:
        return random.uniform(23,40)
    if 8 <= month <= 10:
        return random.uniform(15,30)
    if month == 11 :
        return random.uniform(5,20)


# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.


# ==================================================
# Submit your exercises:
# - Don’t forget to push to Github
# - Submit your exercises to DI Learning
# ==================================================
#
# One Last Thing: Good luck! 🚀
# ==================================================