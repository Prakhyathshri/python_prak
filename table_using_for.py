num = int(input("Enter the table number: "))
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for i in range(start, end+1):
    mul = num * i
    print(f"{num} * {i} = {num}")
