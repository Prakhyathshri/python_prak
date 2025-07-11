tup = (1,2,3)
print(tup)
print("tup[0] = 0") # This operation is not allowed in tuples because Tuples are Immutable.

tup2 = (1)
print(tup2)
print(type(tup2))
# This will be considered at a int, so the solution is we need to use comma while using tuple for single element
tup3 = (1,)
print(tup3)
print(type(tup3))

tuup = (2,4,5,6,2,4,2,6,8,2,2)
print(tuup.index(2))
print(tuup.count(2))