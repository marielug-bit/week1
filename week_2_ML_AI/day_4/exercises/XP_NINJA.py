import json
import re
import random

class MenuManager:
    def __init__(self,file_path):
        with open(file_path,'r') as f:
            self.menu = json.load(f)

    def add_item(self,name,price):
        self.menu['items'].append({"name": name,"price": price})
    
    def remove_item(self,name):
            for k,dic in enumerate(self.menu['items']):
                    if  dic['name']== name:
                        self.menu['items'].pop(k)
                        return True
            return False
        
    def save_to_file(self):
        with open('/Users/mariekrammer/Desktop/week 1 ML AI/week_2_ML_AI/day_4/exercises/restaurant_menu.json','w') as f:
             json.dump(self.menu, f, indent=2)


    def is_valid(self,choice):
        pattern = r"^(?=(?:.*e){2,})(?!.*\d)V[A-Za-z]*(?: (?:[A-Z][a-z]*|of|and|the))*$"
        if re.match(pattern,choice):
             return True
        return False
    
    def print_heart(self):
        heart = [
        "  ***     ***  ",
        " *****   ***** ",
        "******* *******",
        "***************",
        " ************* ",
        "  ***********  ",
        "   *********   ",
        "    *******    ",
        "     *****     ",
        "      ***      ",
        "       *       "
    ]
        print("\n".join(heart))




manager = MenuManager("day_4/exercises/restaurant_menu.json")
print(manager.menu)
print(type(manager.menu))
#manager.add_item("Pasta", 15)
manager.remove_item("Pasta")
manager.save_to_file()




class Character:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    @property
    def strength(self):
        lst = [random.randint(1,6) for i in range(4)]
        sorted_list = sorted(lst)
        return sum(sorted_list[:-2])
    
    @property 
    def dexterity(self):
        lst = [random.randint(1,6) for i in range(4)]
        sorted_list = sorted(lst)
        return sum(sorted_list[:-2])
    
    @property 
    def constitution(self):
        lst = [random.randint(1,6) for i in range(4)]
        sorted_list = sorted(lst)
        return sum(sorted_list[:-2])
    
    @property 
    def intelligence(self):
        lst = [random.randint(1,6) for i in range(4)]
        sorted_list = sorted(lst)
        return sum(sorted_list[:-2])
    

    @property 
    def wisdom(self):
        lst = [random.randint(1,6) for i in range(4)]
        sorted_list = sorted(lst)
        return sum(sorted_list[:-2])
    
    @property 
    def charisma(self):
        lst = [random.randint(1,6) for i in range(4)]
        sorted_list = sorted(lst)
        return sum(sorted_list[:-2])


class Game:
    def __init__(self):
        self.characters = []

    def start_the_game(self):
        num = int(input('How many players want to play ?'))
        list_of_characters = []
        for i in range(num):
            name = input('What is the name of your character ?')
            age = int(input('What is the age of your character?'))
            new_player = Character(name,age)
            list_of_characters.append({'name':new_player.name, 'age': new_player.age, 'strength':new_player.strength,
                           'dexterity':new_player.dexterity, 'constitution':new_player.constitution, 'intelligence':new_player.intelligence,
                            'wisdom':new_player.wisdom, 'charisma':new_player.charisma })
            with open('/Users/mariekrammer/Desktop/DI learning/week_2_ML_AI/day_4/exercises/characters.txt', 'a') as f:
                f.write(f"{new_player} \n")
        with open('/Users/mariekrammer/Desktop/DI learning/week_2_ML_AI/day_4/exercises/characters.json','r') as f:
            json.dump(list_of_characters,f,indent = 4)

                


    
import random
import json

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # stats tirées UNE FOIS
        self.strength = self.roll_stat()
        self.dexterity = self.roll_stat()
        self.constitution = self.roll_stat()
        self.intelligence = self.roll_stat()
        self.wisdom = self.roll_stat()
        self.charisma = self.roll_stat()

    @staticmethod
    def roll_stat():
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(rolls) - min(rolls)   # somme des 3 meilleurs

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
        }

    def to_pretty_text(self, idx=None):
        header = f"Character #{idx}: {self.name}" if idx is not None else f"Character: {self.name}"
        return (
            f"{header}\n"
            f"Age: {self.age}\n"
            f"Strength: {self.strength}\n"
            f"Dexterity: {self.dexterity}\n"
            f"Constitution: {self.constitution}\n"
            f"Intelligence: {self.intelligence}\n"
            f"Wisdom: {self.wisdom}\n"
            f"Charisma: {self.charisma}\n"
            f"{'-'*30}\n"
        )


class Game:
    def __init__(self):
        self.characters = []

    def start_the_game(self):
        num = int(input("How many players want to play? "))

        for i in range(1, num + 1):
            name = input(f"Player {i} - character name: ")
            age = int(input(f"Player {i} - character age: "))
            self.characters.append(Character(name, age))

        self.export_txt("characters.txt")
        self.export_json("characters.json")
        print("Export done: characters.txt + characters.json")

    def export_txt(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("=== D&D Characters ===\n\n")
            for i, c in enumerate(self.characters, start=1):
                f.write(c.to_pretty_text(idx=i))

    def export_json(self, filepath):
        data = [c.to_dict() for c in self.characters]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


# Exemple d'utilisation:
# game = Game()
# game.start_the_game()