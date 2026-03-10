# Instructions: Old MacDonald’s Farm
#
# You are given example code and output. 
# Your task is to create a Farm class that produces the same output.
#
#
# Step 1: Create the Farm Class
#
# Create a class called Farm.
# This class will represent a farm and its animals.

class Farm:

# Step 2: Implement the __init__ Method
#
# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes:
# - name to store the farm’s name
# - animals to store the animals (initialize as an empty dictionary).
#
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}
# Step 3: Implement the add_animal Method
#
# Create a method called add_animal.
# It should take two parameters:
# - animal_type
# - count (with a default value of 1).
#
# Count is the quantity of the animal that will be added to the animal dictionary.
#
# The dictionary will look like this:
# {'cow': 1, 'pig': 3, 'horse': 2}
#
# If the animal_type already exists in the animals dictionary,
# increment its count by count.
#
# If it doesn’t exist, add it to the dictionary as the key
# and with the given count as value.
    def add_animal(self,animal_type,count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
            return
        self.animals[animal_type] = count
#
# Step 4: Implement the get_info Method
#
# Create a method called get_info.
# It should return a string that displays:
# - the farm’s name
# - the animals and their counts
# - the “E-I-E-I-0!” phrase.
#
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.
    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"

        info += "\n    E-I-E-I-0!"

        return info
# Step 5: Test Your Code
#
# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.
#
#
# Example:

#
# Test the code 
#macdonald = Farm("McDonald")
#macdonald.add_animal('cow', 5)
#macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
#macdonald.add_animal('goat', 12)
#print(macdonald.get_info())
#
# output:
# McDonald's farm
#
# cow : 5
# sheep : 2
# goat : 12
#
#     E-I-E-I-0!
#
#
# Bonus: Expand The Farm
#
#
# Step 6: Implement the get_animal_types Method
#
# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types
# (keys from the animals dictionary).
# Use the sorted() function to sort the list.

    def get_animal_types(self):
        animal_types = [animal for animal in self.animals]
        return sorted(animal_types)
#
# Step 7: Implement the get_short_info Method
#
# Add a method called get_short_info to the Farm class.
# This method should return a string like:
# “McDonald’s farm has cows, goats and sheeps.”
#
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name
# if its count is greater than 1.
# Use string formatting to create the output.

    def get_short_info(self):
        animals_list = []

        for animal in self.get_animal_types():
            if self.animals[animal] > 1:
                animals_list.append(animal + "s")
            else:
                animals_list.append(animal)

        if len(animals_list) > 1:
            short = ", ".join(animals_list[:-1]) + " and " + animals_list[-1]
        else:
            short = animals_list[0]

#
# Step 8: Upgrade the add_animal Method
    def add_animal(self,**kwargs):
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty
# Use **kwargs for passing multiple animals.
# The keys will be the animal name and the value will be the quantity.
#
# Then you can call the method this way:
# macdonald.add_animal(cow=5, sheep=2, goat=12)