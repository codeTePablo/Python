# find the tresure island

def statements():
    print("WELCOME TO MAP TO TRESURE, YOU ARE BLIND\n")
    print("You start here\n")
    print("rules to start game: ")
    print("left, right, return, walk")
    
    user = input("please type a direction, left or right")
    if user == "left":
        left = input('here, down or right?').lower()
        if left == "right":
            up = input('up or right')
            if up == "up":
                right = input('you continue in up or right')
                if right == "right":
                    print("you win")
            else:
                print("this is the wrong wat")
        else:
            print("this is the wrong wat")
    else:
        print("you will return")


def test():
    choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
    if choice1 == "left":
      choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
      if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
          print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
          print("You found the treasure! You Win!")
        elif choice3 == "blue":
          print("You enter a room of beasts. Game Over.")
        else:
          print("You chose a door that doesn't exist. Game Over.")
      else:
        print("You get attacked by an angry trout. Game Over.")
    else:
      print("You fell into a hole. Game Over.")

def year():
    year = int(input())
    if year % 4 == 0 and year % 400 == 0:
        print("leap")
    elif year % 100 == 0:
        print("not leap")

def pizza():
    print("HELLO TO LOOTLE PISSA")
    piz = input("Order pizza\n").lower()

    small = 15
    medium = 20
    large = 25
    total = 0
    if piz == "small" or piz == "medium" or piz == "large":
        print((f"you select {piz} pizza"))
        price = input("you want agree more things")
        total += small 
        if price == "yes":
            extra = input('Select the extra: peperoni or chesse')
            if extra == "peperoni":
              print(f"your order a pizza {piz} with {extra}")
              total += 2
            elif extra == "chesse":
              print(f"your order a pizza {piz} with {extra}")
              total += 3
              print(total)
        else:
            print("We will prepared your order")
    else:
        print("thanks for nothing")

def num_count():
  name1 = input('insert the name')
  name2 = input('insert the name')
  names = name1 + name2
  lower_case_string = names.lower()
  
  # count the 
  t = lower_case_string.count("t")
  r = lower_case_string.count("r")
  u =lower_case_string.count("u")
  e = lower_case_string.count("e")
  true = t + r + u + e

  l = lower_case_string.count("l")
  o = lower_case_string.count("o")
  v = lower_case_string.count("v")
  e = lower_case_string.count("e")
  love = l + o + v + e

  score = str(true) + str(love)
  print(score)

if __name__ == '__main__': 
    # statements()
    # test()
    # year()
    # pizza()
    num_count()