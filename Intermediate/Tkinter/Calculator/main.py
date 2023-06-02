# any number of arguments
# def add(*args):
#     # args is a tuple
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# # print(add(1,2,3,4,5,7))

# def calculate(n,**kwargs):
#     # dictionary
#     print(kwargs)
#     # multiple operations assing the data 
#     # n += kwargs["add"]
#     n *= kwargs["add"]
#     print(n)

# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        # self.make = kw["make"]
        # self.model = kw["model"]
        # using get is avoid error if not exist model in model or make 
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make ="Nissan", model = "gt-8")
print(my_car.color) # return None

