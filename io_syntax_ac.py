with open("sample.txt","r")as f:
    data = f.read()
    print(data)

with open("sample.txt","w+")as f:
    f.write("This is new data")
    f.seek(0)
    data = f.read()
    print(data)
    

    '''
    data = f.write("This is new data")
    print(data)

    If we print the write fucntion, it will print the number of changes made not the changes made bcz it is write not read, if we want to read, we need to read it by using w+ mode itself

    '''