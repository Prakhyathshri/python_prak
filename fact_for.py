num = int(input("Enter the number: "))
fact = 1

i = 1
for i in range(1, num+1):
    fact = fact * i

print("Factorial is ", fact)  

# Same code Using while loop 
i = 1
while (i <= num):
    fact *= i
    i += 1
print("Factorial is ", fact)  