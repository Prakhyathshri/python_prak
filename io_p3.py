def check_for_line(word):
    # word = 'jj'
    data = True
    line_no = 1
    with open("practice.txt","r")as f:
        while data:
            data = f.readline()
            if (word in data):
                print("Found at",line_no)  
                return     
            line_no += 1
    print("not found")

check_for_line(input("Enter word to be searched: "))           
