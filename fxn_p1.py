
a = [2,2,2,2,2,2,2,2]
cities = ["Banglore", "Mysore", "Delhi", "Chennai", "Mumbai"]

# WAP using fxns to print the length of the list
def length_list(ls):
    print(len(ls))

# length_list(a)
# length_list(cities)

# WAP using fxns to print the elements of the list in single line
def print_list(ls):
    for item in ls:
        print(item, end=" ")


# print_list(a)
# print_list(cities)

# WAP to find the FACTORIAL of N Using fxn
def find_fact(n):
    # i = 1
    # fact = 1
    # while i <= n:
    #     fact *= i
    #     i += 1
    # print (fact)

    fact = 1
    for i in range(1, n+1):
        fact *= i
    print (fact)

# find_fact(1)
# find_fact(2)
# find_fact(3)
# find_fact(4)
# find_fact(5)
# find_fact(6)
# find_fact(7)
# find_fact(8)
# find_fact(9)
# find_fact(10)

# WAP using fxn to convert USD to INR
def convert(usd):
    print(usd,"$ =",usd*83,"₹")

# convert(float(input("Enter USD: ")))

# WAP using fxn to check if the number is EVEN or ODD
def odd_even(num):
    if(num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

odd_even(int(input("Enter a number to check even or odd: ")))
