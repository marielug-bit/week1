from day_4.exercises.exercice_XP_gold_menu.menu_manager import MenuManager
import json

def load_manager(file_path):
    return  MenuManager(file_path)

def show_user_menu(file_path):
    manager = MenuManager(file_path)
    choice = int(input('Do you want \n 1) add an item, ' \
    '\n 2) Delete an item, \n 3)View the menu, \n 4)Exit \n'))
    if choice ==1:
        name = input('Name of new product')
        price = int(input('price of new product'))
        manager.add_item(name,price)
        manager.save_to_file()
    if choice ==2:
        name = input('name of the product you want to remove')
        if manager.remove_item(name):
            manager.save_to_file()
            print('removed')
        else:
            print('error')
    if choice == 3:
        with open(file_path,'r') as f:
             content = f.read()
        print(content)
    if choice == 4:
       manager.save_to_file()
       with open(file_path,'r') as f:
            menu = f.read()
       print('file saved')


show_user_menu('/Users/mariekrammer/Desktop/week 1 ML AI/week_2_ML_AI/day_4/exercises/restaurant_menu.json')