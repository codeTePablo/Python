import random as rd
def cards():
    """ Returns a random card """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = rd.choice(cards)
    return card

def calculate_score(cards):
    """ Returns the score """
    if sum(cards) >= 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, computer"
    elif user_score == 0:
        return "you win"
    elif user_score > 21:
        return "you went over, u lose"
    elif computer_score > 21:
        return "computer went over"
    

print("black jack")
should_stop = False
while not should_stop:
    ls_user = []
    ls_computer = []

    for _ in range(2):
        ls_user.append(cards())
        ls_computer.append(cards())

    print(ls_user)
    print(ls_computer)

    user_score = calculate_score(ls_user)
    compute_score = calculate_score(ls_computer)
    print(user_score)
    print(compute_score)

    if user_score == 0 or compute_score == 0 or user_score > 21:
        should_stop = True
    else:
        user_deal = input("type y to get another card, type n to pass: ")
        if user_deal == "y":
            ls_user.append(cards)
        else:
            should_stop = True

while compute_score != 0 and compute_score < 17:
    # add card
    ls_computer.append(cards())
    # call function to add new card
    compute_score = calculate_score(ls_computer)

print(compare(user_score,compute_score))
