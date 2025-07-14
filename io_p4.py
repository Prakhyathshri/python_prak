# with open("numbers.txt","w+")as f:
#     f.write("1,2,3,4,5,6,7,8,9")

#     f.seek(0)
#     print(f.read())

#     f.seek(0)
#     text = (f.read())

#     print(text)
#     print(type(text))
#     f.seek(0)

#     str_text = text.split(",")
#     print(str_text)

#     int_text = []

#     for i in str_text:
#         number = int(i)
#         int_text.append(number)

#     print(int_text) 
#     count = 0
#     for i in int_text:
#         if (i % 2 == 0):
#             count += 1

#     print("The total number of even numbers in the list is:",count)


# above all own try
# below all is from video

with open("numbers.txt","r")as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(num)
    #     else:
    #         num += data[i]
    # if num:
    #     print(int(num))

    nums = data.split(",")
    print(nums)

# Now use the same for loop method as I did    



