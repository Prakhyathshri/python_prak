class Student:
    type = "human being"
    clg = "R V University"
    name = "Unknown"
    std = "x"
    marks = "not available"
    # This is class attribute same for all the objects, so we only define it once

    # def __init__(self):
    #     pass
    # This is a default constructor

    def __init__(self,name, std, marks):
        self.name = name
        self.std = std
        self.marks = marks
        print("Adding new student to a Database")
        # These are instance or object attribute, it is specific for each of the object

    def welcome(self):
        print("Welcome Student")   
        print("Welcome Student", self.name)   
    # This is the method     

    def get_marks(self):
        return self.marks

student1 = Student("Yuva","10th",98)
student1.welcome()
print(student1.get_marks())
print(student1.name)
print(student1.std)
print(student1.marks)
print(student1.clg)

student2 = Student("Shri","9th",78)
print(student1.welcome(), student2.name, student2.std, student2.marks, student2.clg)


# print(Student.name, Student.std, Student.marks, Student.clg )


'''
class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)
'''