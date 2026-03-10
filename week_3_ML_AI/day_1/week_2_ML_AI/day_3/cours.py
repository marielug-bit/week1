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

from collections import Counter  
list = [1,2,3,4,1,2,6,7,3,8,1,2,2]  
answer=Counter()
answer = Counter(list)  
print(answer[2])  
print(answer)

from collections import deque  
#initialization
list = ["a","b","c"]  
deq = deque(list)  
print(deq)  

#insertion
deq.append("z")  
deq.appendleft("g")  
print(deq)
#removal
deq.pop()  
deq.popleft()  
print(deq)

import collections

dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps) 

from collections import OrderedDict  
order = OrderedDict()  
order['a'] = 1  
order['b'] = 2  
order['c'] = 3  
print(order)  

#unordered dictionary
unordered=dict()
unordered['a'] = 1  
unordered['b'] = 2  
unordered['c'] = 3 
print("Default dictionary", unordered)
