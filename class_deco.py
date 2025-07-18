class Person:
    name = "xyz"

    @classmethod
    def change_name(cls, name):
        cls.name = name

    # This class method will directly make chnages in the class methods
'''
        def change_name(self, name):
            self.name = name # This will only change the object sttribute and print the xyz only
            Person.name = name # This will change the class attribute and print the name of the input
            self.__class__.name = "Yuva" # This is also another type of doing the above task
'''
p1 = Person()
p1.change_name("Yuva")
print(p1.name)
print(Person.name)