# calculator 
def add(num1, num2):
    """ sum num1 and num2 """
    return num1 + num2

def rest(num1, num2):
    """ rest num1 and num2 """
    return num1 - num2

def prod(num1, num2):
    """ product num1 and num2 """
    return num1 * num2

def div(num1, num2):
    """ divide num1 and num2 """
    return num1 / num2

def operation():
    x = int(input("What's the first number ?: "))
    print("+ - * /")

    # create a dictionary to identify operations 
    operations = {
        "+":add,
        "-":rest,
        "*":prod,
        "/":div
    }
    should_continue = True
    
    while should_continue:    
        op = input("pick an operation: ")
        y = int(input("What's the second number ?: "))
        # declare input symbol to correct function   
        calculation = operations[op]
        # print route to follow
        print(calculation)
        # declare 2 numbers to do operation
        answer = calculation(x,y)
        print(answer)

        user = input(print(f"you want follow with {answer} or new operation to continue ? "))

        if user == "y":
            x = answer
        else:
            should_continue = False
            operation()

if __name__ == "__main__":
    operation()