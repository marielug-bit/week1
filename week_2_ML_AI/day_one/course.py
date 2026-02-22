class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age  = cat_age

# Step 1: Create three cat objects
cat1 = Cat('Marie',10)
cat2 = Cat('David',11)
cat3 = Cat('Yehuda',1)

# Step 2: Write a function to find the oldest cat
#def find_oldest_cat(cat1, cat2, cat3):
    #cats = [cat1,cat2,cat3]
    #cats_age = max([cat.age for cat in cats])
    #for cat in cats:
        #if cat.age == cats_age:
            #print(cat.name) 

def find_oldest_cat(*cats):
    max_age = max(cat.age for cat in cats)
    return [cat for cat in cats if cat.age == max_age]

#def find_oldest_cat(cat1, cat2, cat3):
    #cats = [cat1, cat2, cat3]
    #oldest = max(cats, key=lambda cat: cat.age)
    #return oldest.name

#def find_oldest_cat(*cats):
    #max_age = max(cat.age for cat in cats)
    #return [cat.name for cat in cats if cat.age == max_age]

print([cat.name for cat in find_oldest_cat(cat1, cat2, cat3)])
# Step 3: Print the result
# oldest = find_oldest_cat(cat1, cat2, cat3)
# print(...)

find_oldest_cat(cat1, cat2, cat3)

# 🌟 Exercise 2 — Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')  # print "<name> goes woof!"

    def jump(self):
        print(f"{self.name} jumps {self.height} cm high!")  # print "<name> jumps <height*2> cm high!"

# Step 2: Create dog objects
davids_dog = Dog('Rex',50)
sarahs_dog = Dog('Bella', 35)

# Step 3: Print details and call methods
dogs = [davids_dog, sarahs_dog]
for dog in dogs:
    print(dog.name + ' ' + str(dog.height) )
    dog.bark()
    dog.jump()
# Step 4: Compare sizes
max_heigth = max(dog.height for dog in dogs)
for dog in dogs:
    if max_heigth == dog.height:
        print(f'{dog.name} is higher')

print(max(dogs, key = lambda dog:dog.height))

# 🌟 Exercise 3 — Song

class Song:
    def __init__(self, lyrics : list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
       

# Create a song and call sing_me_a_song()
new_song = Song(['Il etait un petit navire','qui n avait ja-ja-jamais navigue','Oheohe'])
new_song.sing_me_a_song()

# 🌟 Exercise 4 — Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        dic = {}
        for animal in self.animals:
            if animal[0] in dic.keys():
                dic[animal[0]].append(animal)
            dic[animal[0]] = [animal]
            return dic


    def get_groups(self):
        for key,value in self.sort_animals().items():
            print(value)

# Create a zoo and test it
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()
