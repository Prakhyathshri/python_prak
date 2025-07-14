def cal_pro(a=1, b=1):
    print (a * b)
    return a * b

cal_pro() 
# This will now use default parameters defined inside the fucntion
cal_pro (2,2)
# This will not use the default paramters rather will use the arguments passed when calling the fucntion

def pro(a, b=1):
# def pro(a=1, b): #This will give an error
    print (a * b)
    return a * b

pro(1)
# Default arguemnts should always be in the end (last parameters)
