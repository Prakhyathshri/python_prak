# Operations in tuples 
# Converting a tupe to list and list back to tuple

tup = ("a","b","c")
print(tup)
lst=list(tup)
print(lst)
lst.pop(1)
print(lst)
tup=tuple(lst)
print(tup)

names=("yuva","shri")
surnames=("b","s")
fullname=names+surnames
print(fullname)             # Merging two tuples into one is easy
new=len(fullname)
print(new)                  # This is how we can find out the length of the tuple

tuplee=(1,1,1,1,1,1,1,1,3,3,3,4,4,2,2,)
total=tuplee.count(1)
print(total)
tot=tuplee.index(1)         # This finds the first index of 1 in whole tuple
print(tot)
totall=tuplee.index(1,1,9)  # This finds the first index of 1 in the next mentioned index of particlar tuple 
print(totall)
