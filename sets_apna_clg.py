''' Sets are Mutable, but the elements of the sets are Immutable
We will have an option of add removing elements from the set, but no the choice of choosing the INDEX particluary '''

collection = {2,3,4,4,4,"Hello","World","World",1}

print(collection)
print(type(collection))
print(len(collection))

collection.add(7) #Adds an element to the set
print(collection)

collection.remove(7) #Removes the element from the set
print(collection) 

col = set() # Syntax of Creating empty set
col.add(1)
col.add(2)
col.add(2)
print(col)
print(len(col))
col.pop()
print(col)
col.clear()
print(len(col))
print(col)

collection2 = {"namasthe", 77, 34, 22, 22, "HI",1, 2, 3}
print(collection.union(collection2))
print(collection.intersection(collection2))
