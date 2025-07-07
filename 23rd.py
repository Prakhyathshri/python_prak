# LIST METHODS

l = [1,5,45,65,23,1,2,44,563,7,8,3]
print(l)

l.append(5) 
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l = [1,5,45,65,23,1,2,44,563,7,8,3]
print(l)

l.reverse()
print(l)

l = [1,5,45,65,23,1,2,44,563,7,8,3]
print(l)

print(l.index(2))
print(l.index(45))
print(l.index(1))
print(l.index(3))
print(l.index(7))
print(l.index(7))

print(l.count(2))
print(l.count(45))
print(l.count(1))
print(l.count(3))
print(l.count(7))
print(l.count(7))

l = [1,5,45,65,23,1,2,44,563,7,8,3]
print(l)
m = l.copy()
m[0] = 420
print(m)
m.insert(5, 567)
print(m)

print("Hi")
print(l)
print(m)
m.extend(l)     # list l adds after the m list 
print("Hi")
print(l)
print(m)
print("Hello")
a = l + m       # A new list a will be made by merging the list l and list m 
print(a)



# APPEND is a method of  list  - it adds an elemnt at the end of the list
# SORT arranges the list in ascending order
# l.sort(reverse=True) - This arrnges the list in desending order
# REVERSE will ulta palta the original list 
# print(l.index(2)) - this will print the specific index of an list
# print(l.count(7)) - this will count how many times the number has occured it in the list
# m = l.copy() - this is how you make an copy of the list
# m.insert(5, 567) - At 5th index 567 will get inserted 
