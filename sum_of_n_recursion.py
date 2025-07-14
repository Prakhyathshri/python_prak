def find_sum(num):
    if (num == 0):
        return 0
    return find_sum(num-1) + num

print(find_sum(5))

'''
The below is the actual logic for finding Sum of N numbers
    # sum = 1
    # for i in range(1, num):
    #     sum += i
    # return sum
'''
