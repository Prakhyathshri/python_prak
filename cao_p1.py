class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod # DECORATOR - It changes the behavior of normal fucntion
    def hello():  # This is a static method which doesnt want self to be its first parameter
        print("Hello students")


    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"Your average is:",sum/3)

        
s1 = Student("Tony", [78,76,54])
s1.get_average()
s1.hello()