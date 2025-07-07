# Strings are immutable
a="Prak"
print(len(a))
print(a)
print(a.upper()) # This prints the string in upper case
print(a.lower()) # This prints the string in lower case
print(a.replace("Prak","Dupi")) # This replaces the string with the given new string, wherever the name is presnt

b="!! paul !!"
print(b)
print(b.rstrip("!")) # It strips the trailing charcter only

c="virat rohith dhoni"
print(c.split(" ")) # Split creates the list, will learn more about lists in near future

d="i am gustavO, caLL me gus"
print(d.capitalize()) 
# This function is used for capitalizing the first words of the string and also corrects the the string 
print(d.istitle()) # This checks wether the first word is capitalized

q="I Am Gustavo"
print(q)
print(q.istitle()) # This checks wether the first word of all the letters is capitalized or not

q="I am Gustavo"
print(q)
print(q.istitle()) # This checks wether the first word of al the letters is capitalized or not 

print(len(d))
print(len(d.center(50)))
print(d.center(50))
print(d.endswith("gus")) # This checks true or false wether it is ending with the same or not 
print(d.endswith("am",1,4)) 
# This checks true or false wether it is ending with the same or not at particular positons

print(d.startswith("gus")) # This checks true or false wether it is starting with the same or not 

print(d.find("lus")) # This return -1 if it cant fnd the occurance 
print(d.find("gus")) # This returns the first occurance
print(d.index("gus")) # This means find the occurance at any cost
# print(d.index("lus")) # This shows error if it cant find the given value

i="Hello9!"
print(i.isalnum()) # this gives false if there is any specail charter in the string
print(i.isalpha()) # this gives false if there is any specail charter or numbers in the string
i="Hello"
print(i.isalnum()) 
print(i.isalpha()) 
 
print(i.islower()) # It checks wether all the charters are in lower case and gives true if yes and false if no
print(i.isupper()) # It checks wether all the charters are in upper case and gives true if yes and false if no

j="Hello\n"
k="Hello"
print(j.isprintable()) # It gives false becuse of \n which can not be printed
print(k.isprintable()) # it gives true becuse the whole string can be printed

x="     " # using space for white space
y="         " # using tab for white space\
print(x.isspace())
print(y.isspace())

z=("hyyyyyy")
print(z.swapcase()) # This converts lower to upper case or upper case to lower case vice versa
z=("Hyyyyyy")
print(z.swapcase()) # This converts lower to upper case or upper case to lower case vice versa

t="in the, bleak midwinter"
print(t.title()) # This converts the string to title