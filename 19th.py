# BREAK AND CONTINUE STATEMNTS
#1st code
i=0
while(i<10):
    print("5 * ", i+1, " = ", 5 * (i+1))
    i = i + 1

#2ndcode
# In break the LOOP gets skipped
for i in range (15):
    print("5 * ", i, " = ", 5 * (i))
    if (i==10):
        break

print("Fuck off")

#n contiue The ITERATION gets skipped which mean a signle loop and goes to the next loop

for i in range (15):
    if (i==10):
        print("Fuck off")
        continue
    print("5 * ", i, " = ", 5 * (i))

#DO WHILE LOOP

i=0
while True:
    print(i)
    i = i + 1
    if(i%100==0):
        break
