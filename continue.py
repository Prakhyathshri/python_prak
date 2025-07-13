i = 0 
while i < 5:
    if (i == 3):
    # if (i % 2 (!=) or (==) 0): to Skip all the even or add numbers from the list
        i += 1    
        continue # Acts as skip
    print(i)
    i += 1    

# This continue will break out of the loop same as break but it will break the loop only for one iteration, so we need to do the increment in the loop for it to continue the loop as per condition