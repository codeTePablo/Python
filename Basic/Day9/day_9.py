from art import logo

def assing_grades():
    student_scores = {
    #key:value
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
    }   
    student_grades = {}

    for students in student_scores:
        # print(students) return the key in list 
        value = student_scores[students]

        if value >= 90:
            student_grades[students] = "outstanding"
        elif value >= 81:
            student_grades[students] = "exceds Expectations"
        elif value >= 71:
            student_grades[students] = "Acceptable"
        else:
            student_grades[students] = "Fail"

def nesting():
    # only one value in key
    capitals = {
        "France": "Paris"
    }
    # nesting a dictionary in a dictionary
    cities_visited = ["Paris", "Dijon"]
    travel = {
        # "France": [cities_visited]
        # here is nested list 
        "Germany": {"cities_visitied": ["Paris", "German"],
        "total_visits":5}
    }

    #nesting dictionary in a list
    travel = [ 
        {
        "Germany": "Berlin",
        "cities_visitied": ["Paris", "German"],
        "total_visits":5
        }
    ]
    # print key in travel 
    for i in travel:
        print(i)

    
def add_new_country(country_visited, times_visitied, cities_visitied):
    travel_log = [
    {
      "country": "France",
      "visits": 12,
      "cities": ["Paris", "Lille", "Dijon"]
    },
    {
      "country": "Germany",
      "visits": 5,
      "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]

    # empy list 
    new_country = {}
    # in travel_log insert values like a new key with value
    new_country["country"] = country_visited
    new_country["visits"] = times_visitied
    # key and value like a list 
    new_country["cities"] = cities_visitied
    # disctionary in a list add new list
    travel_log.append(new_country)

    # add new key and values
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)


def program():
    """ Main program
    for store names and bids """

    print(logo)
    print("Welcome to the secret auction program.\n")
    bids = {}

    exit_game = False
    while not exit_game:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        # store in a dict key like name and price like value 
        bids[name] = price
        user_exit = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if user_exit == "no":
            find_hightest_bin(bids)
            exit_game = True
        else:
            pass
            # 
            # program()

def find_hightest_bin(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        # assing the bid in key of list 
        # and bid_amount is the value of the list  
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"winner is {winner}")


if __name__ == "__main__":
    # assing_grades()
    # nesting()
    program()