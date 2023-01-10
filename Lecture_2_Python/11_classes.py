#  Python Classes 
# Class is a template for a type of object

class Point():
    def __init__(self, inp1, inp2):
        self.x = inp1
        self.y = inp2
   
                        
p = Point(5,6)

print(p.x)
print(p.y)



class Flight():
    # construction function with default argument self
    def __init__(self, capacity) :
        self.capacity = capacity
        self.pasangers = []

# Creating method for class flight
    def add_pasangers (self, name):
        if not self.open_seats():
            return False
        else :
                self.pasangers.append(name)
        return True
    def open_seats(self):
        return self.capacity  - len(self.pasangers)

persons = ["Raju", "Hemant", "Honey"]
flight =  Flight(2)
for person in persons :
    success = flight.add_pasangers(person)
    if(success):
        print(f"Added {person} to the flight Successfully.")
    else :
        print(f"No Available seats for person {person}.")