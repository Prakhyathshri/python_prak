info = {
    "key" : "value",
    "name" : "Yuva",
    "subject" : ["Python","Java","C"],
    "age" : 35,
    "is_adult" : True,
    "marks" : 96.2,
}
# print(info) This is how we print a Dict as a whole
print(info["name"])
print(info["subject"])
print(info["key"])
print(info["age"])
print(info["is_adult"])
print(info["marks"])

info["surname"] = "Shri"
info["name"] = "Prakhyath"
print(info) #We can reassign the value, it will only ruleover/ overwrite the existing value, We can add a key like above

null_dict = {} #This is empty dict
null_dict["Name"] = "Yuva"
print(null_dict)