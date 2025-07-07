# FUNCTIONS
#program 1 - before using fucntions
a=9
b=8
gmean=(a*b)/(a+b)
print(gmean)

c=3
d=7
gmean2=(c*d)/(c+d)
print(gmean2)

#program 2 - after using funtions
#def means - they are user defined fucntions, which means they will be defined by the users by createing them
def functionName(parameters):
    pass
    #code and statemnts
    print("This is the syntax of fucntions")

def caluclateGmean(a,b):     
#caluclateGmean this is the function name (a,b) they are the arguments
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")  
# This will also affect to all the fucntions whenever used

def isLesser(a,b):
    pass          
#Pass means i will work on it afterwads dont do anything just run the program ignoring this fucntion

a=9
b=8
caluclateGmean(a,b)
isGreater(a,b)
# This is called as CALLING the functions

c=3
d=7
caluclateGmean(c,d)
isGreater(c,d)
