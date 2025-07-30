# Sets methods

a = {1,2,3,4}
b = {4,4,3,5,6,7,8}
# a.add(9)
# print(a)
# a.remove(9)
# print(a)

x = a.pop()  #By this will we understand which element was deleted
print(x)  

print(a.symmetric_difference(b))
print(a.difference(b))
print(b.difference(a))

print(a.isdisjoint(b))
print(a.issuperset(b))
print(a.issubset(b))

c = a.union(b)
print(c)
d = a.intersection(b)
print(d)

print(b.intersection_update(a))

a.update(b)
print(a)

s = {2,4,2,6}
print(s)

e = {"Yuva", 15, False, 4.5}
print(e)

harry = set()
# harry = {}  - This will be a dictornary
print(type(harry))

for value in e:
    print(value)

a.clear
print(a) 
