class Student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math

        # self.percent = str((self.phy + self.che + self.math)/3 ) + "%"

    # def cal_per(self):
    #     self.percent = str((self.phy + self.che + self.math)/3 ) + "%"

    @property
    def percent(self):
            return str((self.phy + self.che + self.math)/3) + "%"

stu1 = Student(98, 98, 98)
print(stu1.percent)

stu1.phy = 86
# print(stu1.phy)
# stu1.cal_per()
print(stu1.percent)  # This will be same as above 
