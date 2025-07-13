# Program to find index of a number or element using while loops

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter the searching number: "))
i = 0
while i < len(nums):
  
    if x == nums[i]:
        print(f"{x} found at index {i}")
        break
    else:
          print("finding")
    i += 1

else:
    print("Not found")

print("End of LOOP")