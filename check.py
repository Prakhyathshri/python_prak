# tax_calculator.py

def calculate_tax(salary):
    return salary * (0.2, 0.1)[salary <= 50000]

# Usage (Remove when doing unit tests)
if __name__ == '__main__':
    salary = float(input("Enter your salary: "))
    tax = calculate_tax(salary)
    print("Your salary is", salary, "and tax for that is", tax)
