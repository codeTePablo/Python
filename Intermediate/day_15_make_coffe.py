print("Machine coffee")

Menu = {
    'espresso': {
        'ingredients': {
            'water':50,
            'coffee':18
        }, 
    'cost':1.5,        
    },
    'latte': {
        'ingredients': {
            'water':200,
            'milk':150,
            'coffee':24
        },
        'cost':1.5,        
    },
    'cappuccino':{
        'ingredients':{
            'water':50,
            'coffee':18
        },
        'cost': 3.0
    }
}

profit = 0
resources_ingredients = {
        'water':300,
        'milk':200,
        'sugar':100
    }

coins = {
        'penny':1,
        'dime':10,
        'nickel':5,
        'quarter':25,
    }

def make_coffee(drink_name, order_ingredients):
    """  """
    for item in order_ingredients:
        resources_ingredients[item] -= order_ingredients
    print(f"here is your {drink_name}")

def transaction(pay, drink_cost):
    """  """
    # 
    if pay >= drink_cost:
        change = pay - drink_cost
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough")
        return False

def resources(order):
    """ check if enough resources to make that drink """
    is_enough = True
    # check in the list the item in resources 
    for item in order:
        # if drink item (water, sugar) is greater than resources (same item [water, sugar])
        if order[item] >= resources_ingredients[item]:
            print(f"not enough {item}")
            is_enough = False
    return is_enough

def report(water, milk, coffee, money):
    """ generated to show tue current resource values """
    print(f"water: {resources_ingredients[water]}, milk: {milk}, coffee: {coffee}, money: {money}")

def coins():
    """ check that the user has inserted enough money and return total """
    # create a sum 
    total = int(input("how many a quartes ?")) * 0.25
    total += int(input("how many a dimes ?")) * 0.10
    total += int(input("how many a nickles ?")) * 0.05
    total += int(input("how many a pennies ?")) * 0.01
    
    return total

machine = True
while machine:
    print("\nTo turn off machine, insert off or insert report to show ")
    print("espresso, latte, cappuccino")
    user = input("what you want?: ")
    # user_money = input("insert money: ")

    if user == "off":
        machine = False
    elif user == "report":
        # report()
        print(f"Water: {resources_ingredients['water']}")
        print(f"Sugar: {resources_ingredients['sugar']}")
        print(f"Milk: {resources_ingredients['milk']}")
        print(f"Profit: {profit}")
    else:
        drink = Menu[user]
        print(drink)
        if resources(drink['ingredients']):
            pay = coins()
            transaction(pay, drink["cost"])

