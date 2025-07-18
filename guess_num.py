import random

target = random.randint(1,10)

while True:
    num = input("Guess the nubmber OR Quit(Q): ")
    if (num == "Q"):
        break
    
    num = int(num)
    if (num == target):
        print("WOW, YOU FOUND IT!")
        break

    elif(num > target):
        print("Your number is greater than target")

    else:
        print("Your number is lesser than target")

print("- - - - - G A M E O V E R - - - - -")

 