f = open("sample.txt","r+")
# f = open("sample.txt","w+")
'''w+ will fully wipe out the data and then when we read it, the file will be empty
'''
# f = open("sample.txt","a+")
'''This will read and append mode, so it means we can append at the end and read the file'''
print(f.write("HI "))
f.seek(0)
print(f.read())
f.close()
