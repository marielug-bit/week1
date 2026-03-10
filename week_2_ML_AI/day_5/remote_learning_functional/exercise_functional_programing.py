class Human:
    def __init__(self,id_number:str, name:str, age:int, priority:bool, blood_type:str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

class Queue:
    def __init__(self):
        self.humans = []
    
    def add_person(self,person):
        if person.priority or person.age > 60:
            self.humans.insert(0,person)
        self.humans.append(person)
    

    def find_in_queue(self, person):
        return self.humans.index(person)
    
    def swap(self, person1, person2):
        #copy_human_list = self.humans[:]
        ind1 = self.find_in_queue(person1)
        ind2 = self.find_in_queue(person2)
        self.humans[ind1] = person2
        self.humans[ind2] = person1

    

