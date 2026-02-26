#Exercise 1
# What is a class?
# A class is a blueprint or template used to create objects.
# It defines attributes (data) and methods (functions) that the objects will have.


# What is an instance?
# An instance is a specific object created from a class.
# It contains the actual data and can use the methods defined in the class.


# What is encapsulation?
# Encapsulation is the concept of bundling data and methods together inside a class.
# It also means restricting direct access to some data to protect it from being modified accidentally.


# What is abstraction?
# Abstraction is the concept of hiding complex implementation details
# and exposing only the necessary parts of an object.
# It helps simplify how we interact with objects.


# What is inheritance?
# Inheritance is a mechanism where one class (child/subclass)
# inherits attributes and methods from another class (parent/superclass).
# It promotes code reuse.


# What is multiple inheritance?
# Multiple inheritance occurs when a class inherits from more than one parent class.
# The child class gains attributes and methods from all parent classes.


# What is polymorphism?
# Polymorphism means "many forms".
# It allows different classes to define methods with the same name,
# where each class provides its own implementation.


# What is method resolution order (MRO)?
# MRO is the order in which Python looks for methods and attributes
# when a method is called on an object.
# It is especially important in multiple inheritance.
# You can see it using: ClassName.mro()

#Exercise 2
import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(suit, value) for suit in suits for value in values]
        
    
    def shuffle(self):
        deck_dic = {'Hearts':set(),'Diamonds':set(),'Clubs':set(),'Spades':set() }
        for card in self.cards:
            deck_dic[card.suit].add(card.value)
        for key,value in deck_dic.items():
            if deck_dic[key] != {'A','2','3','4','5','6','7','8','9','10','J','Q','K'}:
                print('error, missing cards')
                return False
        random.shuffle(self.cards)
    
    def deal(self):
        if not self.cards:
            print("No cards left!")
            return None

        index = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(index)

        


        

