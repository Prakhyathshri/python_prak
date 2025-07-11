# This is to take input of movies name and print it, user will specify how many movies they want to input, using WHILE LOOP 
num = int(input("Enter number of movies: "))
i = 0
movie = []

while i < num:
    movie.append(input(f"Enter Movie name {i + 1}: "))
    i = i + 1

print(movie)

# This is to take input of movies name and print it, user will specify how many movies they want to input, using FOR LOOP 
num = int(input("Enter number of movies: "))
i = 0
list = []

for i in range(num):
    name = input("Enter movie name: ")
    i = i + 1
    list.append(name)

print(list)