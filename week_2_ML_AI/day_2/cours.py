class Pet:
    is_lazy = False #class attribute

    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def make_sound(self):
        print("...")

class Cat(Pet):
    is_lazy = True

    def __init__(self, name : str, age : int,indoor:bool):
        super().__init__(name,age)
        self.indoor = indoor
    
    def make_sound(self):
        print(f"{self.name} says: Meow!")

class Dog(Pet):
    def __init__(self, name : str, age : int,breed:str):
        super().__init__(name,age)
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} says: Woof!")

    def fetch(self,item):
        print(f"{self.name} fetches the {item}!")

cat = Cat("Whiskers", 4, indoor=True)
dog = Dog("Buddy", 2, "Beagle")

cat.description()     # from Pet
cat.make_sound()      # Cat's version
dog.make_sound()      # Dog's version
dog.fetch("ball")

print(Cat.is_lazy)    # True
print(Dog.is_lazy) 

class Dog:
    def __init__(self, name : str, age : int, weight : float, breed : str):
        self.age = age
        self.name = name
        self.weight = weight
        self.breed = breed
    
    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self,other_dog:Dog):
        if self.run_speed() > other_dog.run_speed():
            faster_dog = self
        elif self.run_speed() == other_dog.run_speed():
            print('it is a draw!')
            return
        else:
            faster_dog = other_dog
        print(f"{faster_dog.name} wins!")

class Dogs:
    def __init__(self):
        self.pack = []

    def add_dog(self,dog:Dog):
       self.pack.append(dog)

    def fight_all(self):
        for i in range(len(self.pack)):
            for j in range(i+1,len(self.pack)):
                self.pack[i].fight(self.pack[j])

d1 = Dog("Rex",   4, 20.0, "German Shepherd")
d2 = Dog("Bella", 2, 12.0, "Poodle")
d3 = Dog("Max",   6, 30.0, "Saint Bernard")

pack = Dogs()
pack.add_dog(d1)
pack.add_dog(d2)
pack.add_dog(d3)
pack.fight_all()

class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()
c.__sell()