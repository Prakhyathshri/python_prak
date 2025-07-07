# Lists - They are ordered collection of items
marks = [3,4,2]
print(type(marks))
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])

# Lists can be chnages but tuple cannot be chnaged that is the differnce between them
# You can store any differnt data type in single list

yuva = [1,2,"shri",3.4, True]
print(yuva)
print(yuva[4])
print(yuva[-2]) # This is called negavtive indexing
print(yuva[len(yuva)-2])
print(yuva[5-2])
print(yuva[3])

# hence all four of them gave the same answer as expected
# This is how you convert it to positive indexing

if 5 in yuva:
    print("present")
else:
    print("absent")

# using the IN keyword we can find out weather the partriclur elemnt is present in list

if "shri" in yuva:
    print("present")
else:
    print("absent")

# can use to any datatype, not applicable to single type

print(yuva[:])
print(yuva)
print(yuva[1:4])
print(yuva[1:-1])
print(yuva[0:5:2]) 

# The third one is the JUMP index her 2 is the JUMP INDEX

# LIST COMPERHENSION
lst1=[i for i in range(5)]
print(lst1)

lst2=[i*i for i in range(5)]
print(lst2)

lst3=[i*i for i in range(5) if i%2==0]
print(lst3)