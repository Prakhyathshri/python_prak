#This is a normal fucntion
def show1(n):
    print(n)

show1(5)

'''
This is a fucntion which uses RECURSION
It is like calling a fucntion inside a fucntion itself
'''
def show(n):
    if (n == 0):  #BASE CASE - it is similar to Stopping statement which we use in LOOPs
        return
    print(n) # This is the work of the fucntion
    show(n-1) # This is Calling the fucntio inside the fucntion with the given condition

show(5)
