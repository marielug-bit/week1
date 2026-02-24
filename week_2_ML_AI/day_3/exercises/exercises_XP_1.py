#Exercise_1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    
    def __str__(self):
        return f"{self.amount} {self.currency}s"
    
    def __repr__(self):
        return f"Currency('{self.currency}',{self.amount})"
    
    def __int__(self):
        return int(self.amount)
    
    def __add__(self,other: Currency|int):
        if not isinstance(other,(Currency,int)):
           raise TypeError 
        
        if isinstance(other,Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            
            return self.amount + other.amount
        
        else:
            return self.amount + other

    def __iadd__(self,other: Currency|int):
        if not isinstance(other,(Currency,int)):
           raise TypeError 
        
        if isinstance(other,Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        
            self.amount += other.amount
            return self
        
        else:
            self.amount += other
            return self
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))        # 5 dollars
print(int(c1))        # 5
print(repr(c1))       # 5 dollars
print(c1 + 5)         # 10
print(c1 + c2)        # 15
print(c1)             # 5 dollars

c1 += 5
print(c1)             # 10 dollars

c1 += c2
print(c1)             # 20 dollars

#print(c1 + c3)

#Exercise2
#Exercise3

import string
import random

alphabet = string.ascii_letters
print(''.join([random.choice(alphabet) for i in range(5)]))

#Exercise4
import datetime
today = datetime.datetime.today()
print(today)

#Exercise5
first_of_january = datetime.datetime(2027,1,1)
print(first_of_january)
difference = first_of_january - today
print(difference)

#Exercise6
def time_until_birthday(birthdate:datetime.date):
    today = datetime.date.today()
    next_birthday = datetime.date(today.year,birthdate.month,birthdate.day) 
    
    if next_birthday < today:
        next_birthday = datetime.date(today.year+1,birthdate.month,birthdate.day) 
    
    difference =  next_birthday - today
    print(f'{difference} until your birthday')

time_until_birthday(datetime.date(1998,1,2))

#Exercise7

from faker import Faker
fake = Faker()
empty_user = []

def users(num):
    for i in range(num):
        dic = {}
        dic['name'] = fake.name()
        dic['adress'] = fake.address()
        dic['language_code:'] = fake.language_code()
        empty_user.append(dic)

users(10)
print(empty_user)