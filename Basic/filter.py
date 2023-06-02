numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)
print(list(even_numbers))
