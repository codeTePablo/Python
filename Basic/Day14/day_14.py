from data import data
import random as rn 

print("High or low\n")

def high_low(user, one, second):
    if one > second:
        return user == "a"
    else:
        return user == "b"

game_continue = True
while game_continue:
    account_a = rn.choice(data)
    account_b = rn.choice(data)

    if account_a == account_b:
        account_b == rn.choice(data)

    account_name_one = account_a["name"]
    account_follower_one = account_a["follower_count"]

    account_name_second = account_b["name"]
    account_follower_second = account_b["follower_count"]

    print(f"{account_name_one} vs {account_name_second}\n")

    guess = input("A or B: ").lower()
    score = 0

    correct = high_low(guess,account_follower_one, account_follower_second)
    print(f"{correct}, is correct")

    if correct:
        score += 1
        print(f"yeah, score = {score}")
    else: 
        print("damn, fuck no")
        print(f"You score is {score}")
        game_continue = False