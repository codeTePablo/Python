import random

def rand_name():
    names_string = input("give me names separate with coma, please :)\n")
    # convert string in a list 
    names_list = names_string.split(", ")
    print(names_list)

    select_random = random.choice(names_list)
    print(f"{select_random} will go gym today")

def treasure_map():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    print()
    position = input("Where fo u want to put the reasure? ")

    horizontal = int(position[0])
    vertical = int(position[1])

    select_row = (map[horizontal - 1])
    select_row[horizontal - 1] = "x"

    print(f"{row1}\n{row2}\n{row3}")

def paper_rock_scissors():
    user_choise = int(input("please select, 1 to paper, 2 to rock or 3 to scissors\n"))
    computer_choise = random.randint(1, 3)
    print(f"Computer chooise: {computer_choise}")

    if user_choise == 2 and computer_choise == 3:
        print("you win")
    elif computer_choise == 2 and user_choise == 3:
        print("you lose")
    elif computer_choise > user_choise:
        print("you lose")
    elif user_choise > computer_choise:
        print("you win")
    elif user_choise == computer_choise:
        print("draw")
    else:
        pass
        
if __name__ == '__main__':
    # rand_name()
    # treasure_map()
    paper_rock_scissors()