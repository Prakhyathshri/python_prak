# This program will create a non existing fle and will add the text to it
with open("practice.txt","w+")as f:
    f.write("Hi everyone\nwe are learning File I/O")
    f.write("\nusing Java.\nI like programming in Java")
    f.seek(0)
    data = f.read()
    print(data)
