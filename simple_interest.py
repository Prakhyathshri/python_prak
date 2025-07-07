def simple_interest():
    p = float(input("Enter the principle amount: "))
    r = float(input("Enter the rate of interest per annum: "))
    t = float(input("Enter the time period in years: "))

    si = (p*r*t)/100
    print (si)

simple_interest()

