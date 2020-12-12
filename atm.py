from bank import Bank

# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw


class ATM:
    def __init__(self):
        self.reserve = 10000
        self.bank = Bank()
        self.transactions = ["balance", "deposit", "withdraw"]
        self.currentCard = None
        self.currentPIN = None

    def insertCard(self, card: int) -> None:
        self.currentCard = card
        return

    def insertPIN(self, pin: int) -> None:
        self.currentPIN = pin
        return

    def authenticateUser(self) -> bool:
        return self.bank.pinCheck(self.currentCard, self.currentPIN)

    def showAccounts(self) -> dict:
        return self.bank.accountSelect(self.currentCard)

    def performAction(self, account: str, action: str, amount: int) -> dict:

        buf = {
            "card": self.currentCard,
            "account": account,
            "action": action,
            "amount": amount,
            "reserve": self.reserve,
            "status": None,
            "balance": None,
        }

        if action not in self.transactions:
            buf["status"] = False
        else:
            buf = self.bank.transaction(buf)
            self.reserve = buf["reserve"]

        return buf
