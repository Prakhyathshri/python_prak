''' 
f = open("demo.txt",) 
''' 
# This is same as the below as it the defaul always

f = open("demo.txt", "rt") # By default it will be in the read mode and text mode itself
# data = f.read()
# print(data)
# data2 = f.read(5) # - This means we are reading only 5 letters
# print(data2)

'''
After reading a data for first time we cant again read it bcz the curzor will be in the end. Same happend even in the readline, once it is read it will be in the end of first line, so when we call readline fucntion again, it wll continue from there
'''

line = f.readline()
print(line)
line2 = f.readline()
print(line2)

# print(type(data)) 
f.close() #IT is always a good habit to close the opened file

