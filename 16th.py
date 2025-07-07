x=int(input("Enter a number: "))
print("The entered number is",x)

match x:
    case 0:
        print("case is 0")
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 3:
        print("case is 3")
    case _ if x==4 :
        print("Deafault case 1")
    case _:
        print("Deafault case")

# Underscore is used for default case 
    