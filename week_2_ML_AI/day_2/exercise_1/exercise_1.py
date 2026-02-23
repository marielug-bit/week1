# ==================================================
# Exercises XP
# Last Updated: November 5th, 2025
# ==================================================

# 👩‍🏫 👩🏿‍🏫 What You’ll Learn
# - Inheritance
# - Class methods and attributes
# - Polymorphism
# - Exceptions
# - super() function


# ==================================================
# 🌟 Exercise 1: Pets
# ==================================================

# Key Python Topics:
# - Inheritance
# - Class instantiation
# - Lists
# - Polymorphism


# Instructions:

# Use the provided Pets and Cat classes to create a Siamese breed,
# instantiate cat objects, and use the Pets class to manage them.
# See the example below before diving in.


# --------------------------------------------------
# Step 1: Create the Siamese Class
# --------------------------------------------------

# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed,
# or leave it as is if there are no unique behaviors.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

# --------------------------------------------------
# Step 2: Create a List of Cat Instances
# --------------------------------------------------

# Create a list called all_cats that contains instances of:
# - Bengal
# - Chartreux
# - Siamese
#
# Example:
bengal_obj = Bengal('bengi', 3)
chartreux_obj = Chartreux ('Char',4)
siamese_obj = Siamese('Liam',5)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Give each cat a name and age.


# --------------------------------------------------
# Step 3: Create a Pets Instance
# --------------------------------------------------

# Create an instance of the Pets class called sara_pets,
# passing the all_cats list as an argument.

sara_pets = Pets(all_cats)
# --------------------------------------------------
# Step 4: Take Cats for a Walk
# --------------------------------------------------

# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk()
# method on each cat in the list.
sara_pets.walk()

# ==================================================
# 🌟 Exercise 2: Dogs
# ==================================================

# Goal:
# Create a Dog class with methods for barking,
# running speed, and fighting.


# Key Python Topics:
# - Classes and objects
# - Methods
# - Attributes


# --------------------------------------------------
# Step 1: Create the Dog Class
# --------------------------------------------------

# Create a class called Dog with:
# - name
# - age
# - weight
#
# Implement:
# - bark() method → returns "<dog_name> is barking"
# - run_speed() method → returns weight / age * 10
# - fight(other_dog) method → returns a string indicating
#   which dog won the fight based on:
#   run_speed * weight

class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'
    
    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self,other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name} won the fight.")
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            print(f"{other_dog.name} won the fight.")
        else:
            print('It is a tie.')
        

# --------------------------------------------------
# Step 2: Create Dog Instances
# --------------------------------------------------

# Create three instances of the Dog class with different:
# - names
# - ages
# - weights

d1 = Dog("Rex",   4, 20.0)
d2 = Dog("Bella", 2, 12.0)
d3 = Dog("Max",   6, 30.0)

# --------------------------------------------------
# Step 3: Test Dog Methods
# --------------------------------------------------

# Call the bark(), run_speed(), and fight()
# methods on the dog instances to test functionality.
d1.bark()
d2.bark()
d3.bark()
print(d1.run_speed())
d2.fight(d1)

# ==================================================
# 🌟 Exercise 3: Dogs Domesticated
# ==================================================

# Goal:
# Create a PetDog class that inherits from Dog
# and adds training and tricks.


# Key Python Topics:
# - Inheritance
# - super() function
# - *args
# - random module


# --------------------------------------------------
# Step 1: Import the Dog Class
# --------------------------------------------------

# In a new Python file,
# import the Dog class from the previous exercise.


# --------------------------------------------------
# Step 2: Create the PetDog Class
# --------------------------------------------------

# Create a class called PetDog that inherits from Dog.
#
# Add a trained attribute to the __init__ method,
# with a default value of False.
#
# trained means the dog is trained to do tricks.
#
# Implement:
#
# - train() method:
#     • Prints the output of bark()
#     • Sets trained to True
#
# - play(*args) method:
#     • Prints "<dog_names> all play together"
#     • *args is a list of dog instances
#
# - do_a_trick() method:
#     • Prints a random trick if trained is True
#     • Use this list:
#       tricks = [
#           "does a barrel roll",
#           "stands on his back legs",
#           "shakes your hand",
#           "plays dead"
#       ]
#     • Choose a random trick each time


# --------------------------------------------------
# Step 3: Test PetDog Methods
# --------------------------------------------------

# Create instances of PetDog and test:
# - train()
# - play(*args)
# - do_a_trick()


# ==================================================
# 🌟 Exercise 4: Family and Person Classes
# ==================================================

# Goal:
# Practice working with classes and object interactions
# by modeling a family and its members.


# Key Python Topics:
# - Classes and objects
# - Instance methods
# - Object interaction
# - Lists and loops
# - Conditional statements (if/else)
# - String formatting (f-strings)


# --------------------------------------------------
# Step 1: Create the Person Class
# --------------------------------------------------

# Define a Person class with:
# - first_name
# - age
# - last_name (initialized as empty string)
#
# Add a method called is_18():
# - Returns True if age >= 18
# - Otherwise returns False


# --------------------------------------------------
# Step 2: Create the Family Class
# --------------------------------------------------

# Define a Family class with:
# - last_name attribute
# - members list (empty list of Person objects)


# Add a method called born(first_name, age):
# - Create a new Person object
# - Assign the family’s last name to the person
# - Add the person to the members list


# Add a method called check_majority(first_name):
# - Search members list for a person with that first_name
# - If found:
#     • Call is_18()
#     • If True → print:
#       "You are over 18, your parents Jane and John accept that you will go out with your friends"
#     • Else → print:
#       "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# - Print the family’s last name
# - Print each member’s first name and age


# --------------------------------------------------
# Expected Behavior
# --------------------------------------------------

# Your program should allow you to:
#
# - Create a family with a last name
# - Add members using born()
# - Use check_majority() to verify if someone can go out
# - Display family information using family_presentation()
#
# Don’t forget to test your classes by:
# - Creating a Family instance
# - Adding members
# - Calling each method to verify output