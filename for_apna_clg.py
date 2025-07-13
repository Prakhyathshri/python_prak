# To print the list of elements using for loop

list = [1, 2, 3, 4, 5, 6]

for value in list:
    print(value)

# List of strings
ls = ["a", "b", "c", "d", "e"]

for value in ls:
    print(value)

# We can also use for loop for tuples also

tup = (1,2,3,4,5,6)

for num in tup:
    print(num)

# Using for loop for string
# Using the CHAR we can print the each element of the string seperately

str = "Prakhyath"

for char in str:
    print(char)
else:
    print("END")

# The else in the while loops is totally optional 
count = -10
while(count>3):
    print(count)
    count = count - 1
else:
    print("This is oustide while loop")

# This else is used to do any work outside the while loop 
# This extra else also works for FOR LOOP ALSO 
# ELSE Will not work when we use the BREAK statements
