a = int(input("enter number a: "))
b = int(input("enter number b: "))
def average(a,b):
    print("The average of", a ,"and", b, "is", (a+b)/2)

average(a,b)

#default arguments
def sum(a=2,b=6):
    add=(a+b)
    print("The sum of a and b is",add)

sum(4,5)    #This will chnage the value of both a and b
sum(5)      #This will only chnage the value of a
sum(b=7)    #This will only chnage the value of b

#Keyword arguments
def sub(b=58,a=44):
    minus=b-a
    print(minus)
#Hence we can chnage the order pf the paremeters but by defalt it will be same
#If we ont pass the key value argument it will take the default value that is known as keyword argument


# variable length argument
# program 1 
def average(*numbers):   # It has taken as tuples now
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is",sum/len(numbers))


average(1,4,5,6,7)
average(5,6,7,2,2,4,0,4,4)   # Irrespective of the number of elements it will give the output  

# Program 2
# by using the return value 
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)


c=average(1,4,5,6,7)
print(c)
