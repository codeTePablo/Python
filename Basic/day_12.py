import random as rn 
# global scope

# def increase_enemies():
    # global scope 
    # global enemy
    # enemy += 1
    # print(enemy)
# global variables
# enemy = 1

# global variable 
x = rn.randint(0,100)

def check_answer(x, user):
    if user > x:
        print("too high")
    elif user < x:
        print("too low")
        

def easy():
    """ easy game with ten attempts to guess random number """
    print("Easy mode")
    should_stop = True
    score = 10
    while should_stop:
        # local variable taking global x 
        global x
        user = int(input("Insert a number: "))
        if user != x:
            score -= 1
            print(f"Attempts: {score}")
            check_answer(x,user)
        elif score >= 10:
            print("you lost")
            should_stop = False
        elif user == x:
            print("you win")
            should_stop = False

    
def hard():
    # the same algorithm that above
    pass

print("Number Guessing\n")
print("Guess the number between 0 and 100")

# global variable

print(x)

# user choice 
user_choice = input("Select difficult: ")
try:
    if user_choice == 'easy':
        easy()
    elif user_choice == 'hard':
        hard()
except Exception:
    print("Please insert a valid selection")


# more optimize code
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = rn.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") 

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

# if __name__ == "__main__":
#     increase_enemies()