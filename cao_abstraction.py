class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True        
        self.acc = True        
        print("Car started")

car1 = Car()
car1.start()

'''
Hiding all the implementation deatils of the class is known as ABSTRACTION

Wrapping the data and fucntions into one single unit or capsule (OBJECT) is know was ENCAPSULATION
'''
