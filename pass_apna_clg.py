'''
PASS is like a NULL statement, it will only pass NULL
IT can be used in ifelse also - exception
'''

'''
for i in range(5):
    #empty

print("Something")
'''
# Above will give an error

for i in range(5):
    pass
print("Something")

if i > 5:
    pass
print("Something")