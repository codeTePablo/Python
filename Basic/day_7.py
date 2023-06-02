import random as rn
# from replit import clear 
# use librarie for clean before statements
def check_list():
    

    # for i in chosen_word:
    #     if i == guess:
    #         print("right")
    #     else:
    #         print("wrong")

    # display = []
    # 
    # for _ in range(len_word):
    #     # display.append("_")
    #     # or 
    #     display += "_"

    # guess = input("guess a letter: ").lower()
    # # check in chosen word letter for letter if is the correct word 
    # # and add the letter index display
    # for position in range(len_word):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #         display[position] = letter
    # print(display)

    names = ["pablo", "jose"]
    dead = ["D", "E", "A", "D"]

    chosen_word = rn.choice(names)
    print(chosen_word)
    len_word = len(chosen_word)

    display = []
    for _ in range(len_word):
    # display.append("_")
    # or 
        display += "_"

    # display_dead = []
    # for _ in range(len(dead)):
    #     display_dead += "_"

    stages = ['''D''', '''E''', '''A''', '''D''']

    lives = 4
    end_of_game = False
    while not end_of_game:
        guess = input("guess a letter: ").lower()
        # clear()
        # check in chosen word letter for letter if is the correct word 
        # and add the letter index display
        for position in range(len_word):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1 
            if lives == 0:
                end_of_game == True
                print("you lose")

        
        print(display)
    
        if "_" not in display:
            end_of_game = True
            print("you win")

        print(stages[lives])


if __name__ == '__main__':
    check_list()