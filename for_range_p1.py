print(range(10))

seq = range(5)
for i in seq:
    print(i)

for i in range(10):
    print(i)

for i in range (0, 100, 5):
    print(i)
    
for i in range(0,101,2):
    print(i)
# WE CAN USE THIS TO PRINT ALL THE EVEN AND ODD NUMBERS VERY EASILY UNLIKE OTHER PROGRAMMING LANGUAGES USING THE RANGE FUCNTION

''' range(start, stop, step)
range (0, 100, 5)
[It will start from 0 to 100 skipping 5 numbers]
START - optional, from where range number should star [INCLUDED]
STOP - compulsory, where range should end [EXCLUDED]
STEP - Optional, how many is the step size, how much should it skip, by default it is always 1, if specified it will change '''