# F-strings

letter = "My name is {} and I am from {}"
name = "Prakhyath"
country = "India"
print(letter.format(name,country))
print(letter.format(country,name))  # It becomes ulta to the above
# F-strings

letter = "My name is {1} and I am from {0}"
name = "Prakhyath"
country = "India"
print(letter.format(country,name))

# F - strings means we can put variables inside our string
letter = (f"My name is {name} and I am from {country}")
letter = (f"My name is {{name}} and I am from {{country}}") # When we want to disply the ear f-string or dislay the curly braces

txt="For only {price:.2f} dollors"
print(txt.format(price=49.989898))

price = 45.565656
txt = (f"For only {price:.3f} dollors")
print(txt)

print(f"{2*60}")
print(type(f"{2*60}"))
