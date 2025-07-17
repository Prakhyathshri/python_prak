class Mobile:

    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery
        

    def make_call(self, number):
        if self.battery >= 5:
            print("Calling", number,"from",self.brand,self.model,"...")
            self.battery -= 5
            print("Battery remaining is",self.battery)
        else:
            print("Not enough battery to make a call.")

    def watch_video(self, minutes):
        required_battery = minutes * 2
        if self.battery >= required_battery:
            print("Watching video for",minutes,"minutes on",self.brand,self.model)
            i = 1
            while (i <= minutes):
                self.battery -= 2
                i += 1
            print("Battery remaining is",self.battery)
        else:
            print("Not enough battery to watch a video for",minutes,"minutes")

    def charge(self, amount):
        if (amount + self.battery) >= 100:
            extra_charge = (amount + self.battery) - 100
            print(extra_charge,"is extra")
            battery = 100
            print("Battery full",battery)
        else:
            required_charge = 100 - (amount + self.battery)
            self.battery = (amount + self.battery)
            print("Battery required is",required_charge)
            print("Battery remianing is", self.battery)



m1 = Mobile("MOTO","i2",100)
m1.make_call(987654321)
m1.watch_video(10)
m1.charge(20)
