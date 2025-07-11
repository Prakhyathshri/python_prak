a = "Prakhyath 1"
b = 'Prakhyath 2'
c = '''Prakhyath 3'''
print(a,b,c)
str = "This is a string\nThis is second line"
print(str)

list = [2,1,4,3]
list.append(5) # Adds an element to the end of the list
print(list)
list.sort()
print(list) # Sorts the list in ascending order
list.sort(reverse=True)
print(list) # Sorts the list in descending order
list.reverse()
print(list) # Reveres the whole list into reverse
list.insert(5, 6) # (Index, Element)
print(list) # Add an element 6 to index 5
list.remove(6)
print(list) # Remove will delete the element
list.pop(4)
print(list) # Pop will delete the value of given index 

