class Order:
    def __init__(self,items,price):
        self.items = items
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price
    # Custom class is defined here

o1 = Order("Table",20000)
o2 = Order("Bench",10000)

print(o1 > o2)
# This will return TRUE
