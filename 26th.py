# Good morning problem
import time
t = time.strftime('%H:%M:%S')
print(t)
hour=int(input("Enter hours: "))
# hour=int(time.strftime('%H'))
print(hour)
if 0<= hour<12:
    print("Good morning")
elif 12>= hour <16:
    print("Good afternnon")
elif 16>= hour <20:
    print("Good evening")
elif 20>= hour <=24:
    print("Good night")
else:
    print("Not valid hour")