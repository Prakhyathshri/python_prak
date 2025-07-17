battery =(int(input("Enter remaining battery: ")))
charge =(int(input("Enter charge: ")))
if (charge+battery) >= 100:
    extra_charge = (charge+battery) - 100
    print(extra_charge,"is extra")
    battery = 100
    print("Battery full",battery)
else:
    required_charge = 100 - (charge+battery)
    battery = (charge+battery)
    print("Battery required is",required_charge)
    print("Battery remianing is",battery)
