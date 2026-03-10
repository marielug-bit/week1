from exercise_1 import Dog
import random
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

class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True

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
    def play(self,*args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{' '.join(dog_names)} all play together")

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

    def do_a_trick(self):
        tricks = [
           "does a barrel roll",
           "stands on his back legs",
           "shakes your hand",
           "plays dead"
       ]
        if self.trained:
            choice = random.choice(tricks)
            print(choice)

my_dog = PetDog("Fido", 2, 10)
other_dog = PetDog("buddy", 2, 10)
my_dog.train()
my_dog.play(other_dog)
my_dog.do_a_trick()
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

class Person():
    def __init__(self,first_name,age,last_name=''):
        self.first_name = first_name
        self.age = age
        self.last_name = ''

    def is_18(self):
        return self.age >= 18
# --------------------------------------------------
# Step 2: Create the Family Class
# --------------------------------------------------

# Define a Family class with:
# - last_name attribute
# - members list (empty list of Person objects)

class Family():
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = []

# Add a method called born(first_name, age):
# - Create a new Person object
# - Assign the family’s last name to the person
# - Add the person to the members list

    def born(self,first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
# Add a method called check_majority(first_name):
# - Search members list for a person with that first_name
# - If found:
#     • Call is_18()
#     • If True → print:
#       "You are over 18, your parents Jane and John accept that you will go out with your friends"
#     • Else → print:
#       "Sorry, you are not allowed to go out with your friends."

    def check_majority(self,first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

# Add a method called family_presentation():
# - Print the family’s last name
# - Print each member’s first name and age

    def family_presentation(self):
        print(self.last_name)
        for member in self.members:
            print(f"{member.first_name} is {member.age} years old.")


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

fam = Family("Cohen")
fam.born("David", 17)
fam.born("Sarah", 22)

fam.check_majority("David")
fam.check_majority("Sarah")
fam.family_presentation()