from atm import ATM
import sys

# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
if __name__ == "__main__":

    atm = ATM()

    # main program loop, this assumes that the ATM is powered on
    while(1):

        print("--------------------")
        print("Donghyun Park's ATM")
        print("--------------------")
        print("")

        # card number and PIN identification loop
        while(1):
            # valid card number verification
            while(1):
                card = input("Insert 8-digit Card Number: ")
                if len(card) != 8:
                    print("")
                    print("ERROR: Please enter a 8-digit card number")
                    print("")
                    continue
                else:
                    print("Processing card...")
                    atm.insertCard(int(card))
                    break

            print("")
            # valid PIN verification
            while(1):
                pin = input("Insert 4-digit PIN: ")
                if len(pin) != 4:
                    print("")
                    print("ERROR: Please enter a 4-digit card number")
                    print("")
                    continue
                else:
                    print("Processing PIN...")
                    atm.insertPIN(int(pin))
                    break

            print("")
            print("Please wait while verifying Card Number and PIN...")
            print("")

            if atm.authenticateUser():
                print("")
                print("Authenticated!")
                print("")
                break
            else:
                print("")
                print("ERROR: Could not verify Card Number and PIN!")
                print("")
                continue

        # valid accounts fetching loop
        while(1):
            print("")
            print("Fetching Accounts...")
            print("")
            accounts = atm.showAccounts()
            if not accounts:
                print("")
                print(
                    "ERROR: This Card Number has no associated Accounts. Please restart program with valid Card Number and PIN")
                print("")
                sys.exit()
            else:
                for account in accounts:
                    print(account)

                # account decision loop
                while(1):
                    select = input(
                        "Please select an account for this transaction: ")
                    if select not in accounts:
                        print("")
                        print("ERROR: This account is not a valid choice!")
                        print("")
                        continue
                    else:
                        break
                break

        # transaction loop
        while(1):

            print("")
            action = input(
                "For your " + select + " account, please select your transaction (balance/deposit/withdraw): ")

            if action == "balance":
                res = atm.performAction(select, action, 0)
                print("Current Balance: " + str(res["balance"]))
            elif action == "deposit" or action == "withdraw":
                amount = int(input("Enter the amount to process: "))
                res = atm.performAction(select, action, amount)
                if res["status"] == False:
                    print("")
                    print("ERROR: Transaction failed!")
                    print("")
                else:
                    print("")
                    print("Transaction succeeded.")
                    print("Current Balance: " + str(res["balance"]))
            else:
                print("")
                print("ERROR: Please choose a valid transaction!")
                print("")
                continue

            # additional transaction loop
            while(1):
                print("")
                another = input(
                    "Would you like to perform another transaction? (y/n): ")
                if another == "y" or another == "n":
                    break
                else:
                    print("")
                    print("ERROR: Please choose a valid option!")
                    print("")
                    continue
            if another == "y":
                continue
            elif another == "n":
                print("")
                print("Thank you for using our service. Please come again!")
                print("")
                break
            break

        break
