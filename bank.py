fakeBank = {
    12345678: {
        "pin": 2468,
        "accounts": {
            "checking": 1000,
            "saving": 100
        }
    },
    10001000: {
        "pin": 1234,
        "accounts": {
            "checking": 2000,
            "saving": 200
        }
    },
    20002000: {
        "pin": 0000,
        "accounts": {
            "checking": 3000,
            "saving": 300
        }
    },
}

# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw


class Bank():
    def __init__(self):
        pass

    def pinCheck(self, card, pin):
        if card in fakeBank:
            return pin == fakeBank[card]["pin"]
        else:
            return False

    def accountSelect(self, card):
        if card in fakeBank:
            return fakeBank[card]["accounts"]
        else:
            return None

    def transaction(self, items):
        '''
        items = {
            "card": self.currentCard,
            "account": account,
            "action": action,
            "amount": amount,
            "reserve": self.reserve,
            "status": None,
            "balance": None,
        }
        '''

        if items["amount"] < 0:
            items["status"] = False
            return items

        if items["action"] == "balance":
            items["status"] = True

        #fakeBank[card][account] += amount
        elif items["action"] == "deposit":
            fakeBank[items["card"]]["accounts"][items["account"]
                                                ] += items["amount"]
            items["reserve"] += items["amount"]
            items["status"] = True

        #fakeBank[card][account] -= amount
        elif items["action"] == "withdraw":
            # overdraw or not enough money in atm
            if items["amount"] > fakeBank[items["card"]]["accounts"][items["account"]] or items["amount"] > items["reserve"]:
                items["status"] = False
            else:
                fakeBank[items["card"]]["accounts"][items["account"]
                                                    ] -= items["amount"]
                items["reserve"] -= items["amount"]
                items["status"] = True

        items["balance"] = fakeBank[items["card"]
                                    ]["accounts"][items["account"]]
        return items
