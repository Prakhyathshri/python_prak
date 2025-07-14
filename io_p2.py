with open("practice.txt","r")as f:
    data = f.read()
    print(data)

new_data = data.replace("Java", "Python")
print(new_data)
# AT this step the data will not to changed in file, it is only showing in the output, to make chnages in the file, we need to overwrite the file

with open("practice.txt","w+")as f:
    f.write(new_data)
    f.seek(0)
    print(f.read())
# Now this is changed in the file

def check_word(word):
    # word = "learning"
    with open("practice.txt","r")as f:
        data = f.read()
        if(data.find(word) != -1):
            print("FOUND")
        else:
            print("NOT FOUND")
        
check_word("learning")