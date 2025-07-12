# This is NESTED DICT
student = {
    "name" : "Yuva",
    "Subjects" : {
        "phy" : 56,
        "che" : 45,
        "bio" : 67,
        "math" : 34
    }
}
print(student)
print(student["Subjects"])
print(student["Subjects"]["phy"]) 
# We can access the exact keys when we have the nested dicts, and this is how we do it

print(len(list(student.keys())))
# This willthe length of the keys of the nested dict that is the subject's 

student.update({"City" : "Bengaluru"})
student["Subjects"].update({"Eng" : 44})
print(student)
print(student["Subjects"])
print(student["Subjects"]["Eng"]) 