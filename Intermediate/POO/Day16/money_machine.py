class MoneyMachine():

    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self) -> None:
        self.profit = 0
        self.money_received = 0

    def report(self):
        """ Prints the current profit """
        print(f"Money: {self.profit}")

    def process_coins(self):
        """ Returns the total calculated from coins inserted. """

        for coin in self.coins:
            # increase money_received = user insert coin * check coin[coin]
            self.money_received += int(input(f"How many {coin}?: ")) * self.coins[coin]
        return self.money_received

    def make_payment(self, cost):
        """ Returns True when payment is accepted, or False if insufficient. """
        self.process_coins()
        if self.money_received >= cost:
            change = self.money_received - cost
            print(f"here is {change} in change")
            self.profit += cost
            self.money_received = 0
            return True
        else: 
            print("not enough")
            return False
        self.money_received = 0
