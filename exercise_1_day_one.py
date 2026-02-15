# =========================================
# Exercise 1: Hello World
# =========================================

# Print the following output using one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
print('Hello world\n' *4)

# =========================================
# Exercise 2: Some Math
# =========================================

# Calculate the result of (99^3)*8
# In Python, ^ is NOT power. We use ** for exponent.
print((99**3)*8)


# =========================================
# Exercise 3: What is the output?
# =========================================

# Instructions:
# Predict the output of the following code snippets.
# Comment what your guess is, then run the code and compare.

# Example:
# >>> 15 < 8  #False
# >>> 5 < 3 #False
# >>> 3 == 3 #True
# >>> 3 == "3" #False
# >>> "3" > 3 #typeError
# >>> "Hello" == "hello" #False

# =========================================
# 🌟 Exercise 4: Your computer brand
# =========================================

# Instructions:
# Create a variable called computer_brand
# The value should be the brand name of your computer.
# Using the computer_brand variable,
# print a sentence that states:
# "I have a <computer_brand> computer."
computer_brand = 'Mac'
print(f'I have a {computer_brand} computer.')

# =========================================
# 🌟 Exercise 5: Your information
# =========================================

# Instructions:
# Create a variable called name and set it to your name.
# Create a variable called age and set it to your age.
# Create a variable called shoe_size and set it to your shoe size.
# Create a variable called info.
# The value of info should be an interesting sentence about yourself.
# The sentence must contain name, age, and shoe_size.
# Print the info message.
name = 'Marie Sarah'
age = 27
shoe_size = 39
info = f'My name is {name}, I am {age} and my shoe_size is {shoe_size}.'
print(info)

# =========================================
# 🌟 Exercise 6: A & B
# =========================================

# Instructions:
# Create two variables, a and b.
# Each variable should contain a number.
# If a is bigger than b,
# print "Hello World".
a = 3
b = 1
if a > b:
    print("Hello World")

# =========================================
# Exercise 7: Odd or Even
# =========================================

# Instructions:
# Ask the user for a number.
# Determine whether the number is odd or even.
# Print the result.
number = int(input('Choose a number.'))
if number%2 == 0 :
    print ('The number is even')
else : 
    print('The number is odd')


# =========================================
# 🌟 Exercise 8: What’s your name?
# =========================================

# Instructions:
# Ask the user for their name.
# Determine whether the user has the same name as you.
# Print a funny message depending on the outcome.
my_name = 'marie sarah'
user_name = input('What is your name ?').lower()
if my_name == user_name:
    print('What a coincidence, we have the same name !')
else:
    print('We do not have the same name.')



# =========================================
# 🌟 Exercise 9: Tall enough to ride
# =========================================

# Instructions:
# Ask the user for their height in centimeters.
# If the height is over 145 cm,
# print that they are tall enough to ride.
# Otherwise,
# print that they need to grow some more to ride.
user_height = int(input('What is you height in cm?'))
if user_height > 145:
    print('you are tall enough to ride.')
else :
    print('you need to grow some more to ride.23')