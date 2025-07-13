# This program takes input from the user, of which table from which number to which number should I print the multiplication table

num = int(input("Enter the table number: "))
start = int(input("Enter the starting number of the table: "))
end = int(input("Enter the ending number of the table: "))
mul = int()

while start <= end :
    mul = num * start
    print(f"{num} * {start} = {mul}")
    start += 1
