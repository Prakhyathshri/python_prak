info = {
    "key" : "value",
    "name" : "Yuva",
    "subject" : ["Python","Java","C"],
    "age" : 35,
    "is_adult" : True,
    "marks" : 96.2,
}

print(info.keys())
# This is how we can get all the keys in format of lists
print(list(info.keys()))
#This converts the dict keys into lists and gives
print(len(info)) # Gives the len of key value pair

print(info.values()) 
# This will print all the values stored in the dict

print(info.items()) 
#This will retrun all the key value pair as TUPLE
ls = (list(info.items()))
# We can convert this into list 
print(ls[1])

print(info.get("key")) #This will retrun empty none when we have wrong key
print(info["key"]) #This will give error when we dont have any key
# Both of them will give same values