# ==================================================
# Exercise 1: Bank Account
# ==================================================
#
# Instructions
#
# --------------------------------------------------
# Part I:
# --------------------------------------------------
#
# Create a class called BankAccount that contains the following attributes and methods:
class BankAccount():
    def __init__(self,balance):
        self.balance = balance
    
    def deposit(self,num:int):
        if num <= 0 :
            raise Exception
        self.balance += num
    
    def withdraw (self,num):
        if num <= 0 :
            raise Exception
        self.balance -= num

# - balance (an attribute)
#
# - __init__ :
#   initialize the attribute
#
# - deposit (a method):
#   accepts a positive int and adds to the balance,
#   raise an Exception if the int is not positive.
#
# - withdraw (a method):
#   accepts a positive int and deducts from the balance,
#   raise an Exception if not positive
#
#
# --------------------------------------------------
# Part II : Minimum balance account
# --------------------------------------------------
#
# Create a MinimumBalanceAccount that inherits from BankAccount.
#
# Extend the __init__ method and accept a parameter called minimum_balance
# with a default value of 0.
#
# Override the withdraw method so it only allows the user to withdraw money
# if the balance remains higher than the minimum_balance,
# raise an Exception if not.
class MinimumBalanceAccount(BankAccount):
    def __init__(self,balance,username,password,authenticated = False,minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
        self.username = username
        self.password = password
        self.authenticated = authenticated
#
    def withdraw (self,num):
        if num <= 0:
            raise Exception
        
        potential_balance = self.balance - num
        if potential_balance > self.minimum_balance:
            self.balance -= num
        else:
            raise Exception
# --------------------------------------------------
# Part III: Expand the bank account class
# --------------------------------------------------
#
# Add the following attributes to the BankAccount class:
# - username
# - password
# - authenticated (False by default)
#
# Create a method called authenticate.
# This method should accept 2 strings : a username and a password.
# If the username and password match the attributes username and password
# the method should set the authenticated boolean to True.
#
# Edit withdraw and deposit to only work if authenticated is set to True,
# if someone tries an action without being authenticated raise an Exception

    def authenticate(self,username,password):
        if self.username == username and self.password == password:
            self.authenticated = True
    
    def withdraw (self,num,username,password):
        if self.authenticated: 
            if num <= 0:
                raise Exception
        
            potential_balance = self.balance - num
            if potential_balance > self.minimum_balance:
                self.balance -= num
            else:
                raise Exception
        else:
            raise Exception

# --------------------------------------------------
# Part IV: BONUS Create an ATM class
# --------------------------------------------------
class ATM:
    def __init__(self, account_list, try_limit):
        
        # Vérifier que c'est bien une liste
        if not isinstance(account_list, list):
            raise TypeError("account_list must be a list")
        
        # Vérifier que chaque élément est un compte valide
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise TypeError("All items must be BankAccount or MinimumBalanceAccount instances")
        
        # Vérifier que try_limit est un entier positif
        if not isinstance(try_limit, int) or try_limit <= 0:
            raise ValueError("try_limit must be a positive integer")
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
# __init__:
# - Accepts the following parameters: account_list and try_limit.
#
# - Validates that account_list contains a list of BankAccount or
#   MinimumBalanceAccount instances.
#   Hint: isinstance()
#
# - Validates that try_limit is a positive number,
#   if you get an invalid input raise an Exception,
#   then move along and set try_limit to 2.
#   Hint: Check out this tutorial
#
# - Sets attribute current_tries = 0
#
# - Call the method show_main_menu (see below)
#
#
# Methods:
#
# show_main_menu:
# - This method will start a while loop to display a menu letting a user select:
#   • Log in:
#     Will ask for the users username and password and call the log_in method
#     with the username and password (see below).
#   • Exit.
    def show_main_menu(self):
        while True:
            print("\n===== ATM MAIN MENU =====")
            print("1. Log in")
            print("2. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)

            elif choice == "2":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

#
# log_in:
# - Accepts a username and a password.
#
# - Checks the username and the password against all accounts in account_list.
# - If there is a match (ie. use the authenticate method),
#   call the method show_account_menu.
# - If there is no match with any existing accounts,
#   increment the current tries by 1.
#   Continue asking the user for a username and a password,
#   until the limit is reached (ie. try_limit attribute).
#   Once reached display a message saying they reached max tries
#   and shutdown the program.
#
def log_in(self, username, password):

    current_tries = 0

    while current_tries < self.try_limit:

        # Check each account
        for account in self.account_list:
            account.authenticate(username, password)

            if account.authenticated:
                print("Login successful!")
                self.show_account_menu(account)
                return   # Stop the method after success

        # If no account matched
        current_tries += 1
        print("Invalid username or password.")

        if current_tries < self.try_limit:
            print(f"Attempts left: {self.try_limit - current_tries}")
            username = input("Enter username: ")
            password = input("Enter password: ")

    # If limit reached
    print("Maximum login attempts reached. ATM shutting down.")
    exit()
# show_account_menu:
# - Accepts an instance of BankAccount or MinimumBalanceAccount.
# - The method will start a loop giving the user the option to:
#   • deposit
#   • withdraw
#   • exit