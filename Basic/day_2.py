def basic_calculator():
    print("Welcome to the tip calculator\n")
    total_bill = float(input("What was the total bill? "))
    fork = int(input("How many people to split the bill? "))
    porcent = int(input("What percentage tip would you like to give? "))

    per = porcent / 100
    my_part = total_bill * per
    total = my_part + total_bill
    pay = total / 5 

    print(f"The total is: ${pay}")

def add_digits():
    one = (input("input a number of 2\n"))

    digit_one = one[0]
    digit_two = one[1]

    final = int(digit_one) + int(digit_two)
    print(final)

def bmi():
    weight = int(input("insert your weight: \n"))
    height = float(input("insert your height: \n"))

    formula = (int(weight)/float(height**2))
    print(formula)

if __name__ == '__main__':
    add_digits()