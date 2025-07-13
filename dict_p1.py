marks = {}

phy = int(input("Enter phy marks: "))
marks.update({"phy": phy})
che = int(input("Enter che marks: "))
marks.update({"che": che})
maths = int(input("Enter maths marks: "))
marks.update({"maths": maths})

print(marks)

# This program is to print same number twice in sets, as duplicates are not allowed in the sets
same = {
        ("int",9),
        ("float",9.0)
    }
same2 = {9,"9.0"}
print(same)
print(same2)
print(type(same))