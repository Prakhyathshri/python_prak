class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Yuva")
print(s1.name)
'''
del s1 #DEL keyword can delete any object
print(s1.name) #This will give an error
'''
# Here in the above code, the name attribute is PUBLIC as we can access the attributes outside the clsss Student also

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass 
        #Adding two self.__acc_pass will make it a private attribute, so we can only access it inside the class

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account(12345, "abcd")
print(acc1.acc_no)
acc1.reset_pass()

'''
print(acc1.acc_pass) 
#So if we keep the passoword public, anyone can see the password, so we need to keep it private 
'''

class Person:
    __name = "ananoymous"

    def __hello(self):
        print("Hello")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
# print(p1.__name) 
# This will give an error as it a private method 
# print(p1.__hello())
# This will also give error as it is a priavte method