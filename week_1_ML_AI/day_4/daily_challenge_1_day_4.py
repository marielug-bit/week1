# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    if not menu_dict:
        print("The menu is empty.")
        return
    print('Current menu: ')
    for key,value in menu_dict.items():
        print(f'{key} - {value}₪')



def add_item(menu_dict):
    """Add a new drink to the menu."""
    new_drink = input('Enter new drink name: ')
    new_price = input('Enter price: ')
    if new_drink in menu_dict: 
        print("Item already exists!")
        return
    menu_dict[new_drink] = float(new_price)
    print(f'{new_drink} added!')


def update_price(menu_dict):
    """Change the price of an existing drink."""
    drink = input("Which drink's price do you want to update?")
    if not drink in menu_dict:
        print("Item not found.")
        return
    price = float(input('New price: '))
    menu_dict[drink] = price
    print("Price updated!")



def delete_item(menu_dict):
    """Remove a drink from the menu."""
    drink = input('Which drink do you want to remove drom the menu? ')
    if not drink in menu_dict:
        print("Item not found.")
        return
    del menu_dict[drink]
    print("Item deleted.")


def show_options():
    """Print the available actions."""
    print('What would you like to do?')
    print('1. Show menu')
    print('2. Add item')
    print('3. Update price')
    print('4. Delete item')
    print('5. Exit')


def run_coffee_shop():
    """Main loop of the program."""
    # TODO
    while True:
        show_options()
        call = int(input('Choose an action and write the ' \
        'corresponding number of this action'))
        if call == 1:
            show_menu(menu)
        if call == 2:
            add_item(menu)
        if call == 3:
            update_price(menu)
        if call == 4:
            delete_item(menu)
        if call == 5:
            print('Goodbye')
            break
        
        
    


# Start the program
run_coffee_shop()