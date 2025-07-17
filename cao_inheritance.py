'''
INHERITANCE - When a child class derives properties or methods from the parent class it is known as inheritance
'''

class Car:
    def __init__(self, wheels):
        self.wheels = wheels

    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Innova(ToyotaCar):
    def __init__(self,name,color,type,brand):
        self.name = name
        self.color = color
        self.type = type
        super().__init__(brand)
        super().start()

brand1 = ToyotaCar("Toyota")
print(brand1.brand)
brand1.start()
brand1.stop()

car1 = Innova("yuva","Black","Hybrid","Toyota")
print(car1.name, car1.color, car1.type)
print(car1.brand)
# car1.start()
car1.stop()
