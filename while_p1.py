# WAP to find the sum of first N Natural number using while (from 1 to 5)

num = int(input("Enter the number N: "))
sum = 0
i = 0
while(i <= num):
    sum += i
    i += 1
print("Total sum is ", sum)

# Same using for loop
# for i in range(1, num+1):
#     sum += i
    
# print("Total sum is ", sum)
