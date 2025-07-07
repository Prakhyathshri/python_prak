names=("yuva,prak,dhrupad")
print(names[0:6])
# Here from 0 to 6 the 5th elemnt will not be given it is only 0,1,2,3,4,5 that is 1st[0] - y, 2nd[1] - u, 3rd[2] - v, 4th[3] - a, 5th[4] - , , 6th[5] - p

print(names[:6])
# Deafult python will take the 0 if we dont put anything before

print(names[2:6])
# We can also choose from which letter to get started with the printing and which letter to end

print(len(names))
# we can use LENGTH funtion to count the number of elemnts in an string 

print(names[0:-3])
# So here if we give minus python automatically consider the below code so it subtracts the given number from the total length of the array
print(names[0:len(names)-3])

print(names[-1:-3],"Hi") 
# This makes no sense as it shows as 17-1=16 and 17-3=14 so it becomes 16 to 14 bacwise so it will leave blank space

print(names[-4:-2])
# Now it becomes 14 to 16 henc it will run 
# inlcuding 14 but not 16 so only 2 letters it will run



