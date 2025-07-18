import random
import string

pass_len = 12
combine = string.ascii_letters + string.digits + string.punctuation


# using list compherension - This will automatically add itself to the list
# password = [random.choice(combine) for i in range(pass_len)]
password = "*".join([random.choice(combine) for i in range(pass_len)])
'''
password = ""
for i in range(pass_len):
    password += (random.choice(combine))
'''

print("Your password is:",password)
