# TUPLES 
# Tuples and strings are immutable only lists are mutable
# You cannot change or alter the tuple like lists
# There is only one differnce mentioned above other than that it is similar to tuple

tup = (5,4,34,5,6,337)
print(type(tup),tup)
print(tup[1])
print(tup[0])
print(tup[-2])          # Same way negative indexing also works like in lists
print(len(tup))

if 4 in tup:
    print("yes")
else:
    print("no")

tup2 = tup[0:3]
print(tup2)             # A new tuple gets created 

tu = (5)        
print(type(tu),tu)  # It becomes int 

t = (5,)
print(type(t),t)    # You have to use comma if you want to define one element as tuple 
