import json

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


manager = MenuManager("day_4/exercises/restaurant_menu.json")
print(manager.menu)
print(type(manager.menu))
#manager.add_item("Pasta", 15)
manager.remove_item("Pasta")
manager.save_to_file()