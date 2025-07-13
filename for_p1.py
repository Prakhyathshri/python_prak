list1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49)


''' This type of finding is LINEAR SEARCH, searching each and every element in order, there are other type of searching also '''
# for i in list1:
#     print(i)

x = int(input("Enter the searching number: "))
for idx, value in enumerate(list1):
    if (x == value):
        print("x found at ", idx)
        # break
    print("finding.... at index ",idx)
else:
    print("Not Found")

# we can use break if we want the number to searched only once 