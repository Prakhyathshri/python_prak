nums = list(map(int, input("Enter the numbers of list with spaces: ").split()))
list2 = nums.copy()
list2.reverse()
if nums == list2:
    print("It is palindrome")
else:
    print("Not palindrome")
