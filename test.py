from atm import ATM
from bank import Bank
import unittest


class atmTest(unittest.TestCase):
    def testATM(self):
        atm = ATM()
        # ATM holds expected amount
        self.assertEqual(atm.reserve, 10000)

    def testCard(self):
        atm = ATM()
        # valid card
        atm.insertCard(10001000)

        self.assertEqual(atm.currentCard, 10001000)

    def testAuthentication(self):
        atm = ATM()
        # invalid card and invalid pin
        atm.insertCard(87654321)
        atm.insertPIN(0000)

        self.assertEqual(atm.authenticateUser(), False)

        # valid card but invalid pin
        atm.insertCard(10001000)

        self.assertEqual(atm.authenticateUser(), False)

        # valid card and valid pin
        atm.insertPIN(1234)

        self.assertEqual(atm.authenticateUser(), True)

    def testAccounts(self):
        atm = ATM()
        bank = Bank()
        # invalid card
        atm.insertCard(87654321)

        self.assertEqual(atm.showAccounts(), None)

        # valid card
        atm.insertCard(12345678)

        self.assertEqual(atm.showAccounts(), bank.accountSelect(12345678))

    def testTransaction(self):
        transactions = ["balance", "deposit", "withdraw"]

        atm = ATM()
        bank = Bank()

        # valid card and valid PIN
        atm.insertCard(10001000)
        accounts = atm.showAccounts()

        # invalid transaction
        for account in accounts:
            res = atm.performAction(account, "wire", 100)
            self.assertEqual(res["status"], False)
            res = atm.performAction(account, "withdraw", 1000000)
            self.assertEqual(res["status"], False)

        # valid transaction
        for account in accounts:
            for transaction in transactions:
                res = atm.performAction(account, transaction, 100)
                self.assertEqual(res["status"], True)


if __name__ == "__main__":
    unittest.main()
