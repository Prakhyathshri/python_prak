def area_of_square(side):
    area = side*side 
    return area

side = int(input("Enter the length of the square: "))
area = area_of_square(side)
print("The area of the square is:",area)
