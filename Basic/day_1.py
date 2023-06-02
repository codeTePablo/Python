import random
def nameGen():
    try:
        # b = randint()
        print("Welcome to name generator: ")
        street = input("You street name is?... ")
        pet = input("The name of your name dog is?... ")
        a = []
        b = pet
        for i in street:
            print(random.choice(street))
            a.append(random.choice(street))

        print(a)
        print("your user name is: " +  str(a) + " " + b)

    except AssertionError as error:
        print(error)

if __name__ == '__main__':
    nameGen()