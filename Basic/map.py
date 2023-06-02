# Map


def cube(number):
    """cube of number"""
    return number**3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)  #  call function and list of anything
#  itera en cada uno de los elementos de index en la lista
print(list(cubed_numbers))  #  print list
#  [1, 8, 27, 64, 125]

## Multiple map


def add(a, b):
    return a + b


odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
#  unpack them using *
print(*totals, sep=", ")
#  3, 7, 11, 15, 19

##  Using lambdas

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(
    lambda number: number**3, numbers
)  # number (int): number pow 3, for each number
print(list(cubed_numbers))
#  [1, 8, 27, 64, 125]

#  Operator add

from operator import add

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19
