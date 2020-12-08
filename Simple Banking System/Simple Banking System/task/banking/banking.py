import string
import secrets


class Bank:
    def __init__(self):
        self.accounts = []
        self.menuexit = False

    @staticmethod
    def print_main_menu():
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit\n")

    @staticmethod
    def print_login_menu():
        print("1. Balance")
        print("2. Log out")
        print("0. Exit\n")

    def menu(self):
        while not self.menuexit:
            self.print_main_menu()
            menuitem = int(input())
            if menuitem == 1:
                self.accounts.append(BankAccount())
            elif menuitem == 2:
                if self.login():
                    while True:
                        self.print_login_menu()
                        menuitem = int(input())
                        if menuitem == 1:
                            print("Balance: 0\n")
                            pass
                        elif menuitem == 2:
                            print("You have successfully logged out!\n")
                            break
                        elif menuitem == 0:
                            self.menuexit = True
                            print("Bye!")
                            break
                else:
                    print("Wrong card number or PIN!\n")
            elif menuitem == 0 or self.menuexit:
                print("Bye!")
                break

    def login(self):
        number = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")

        for account in self.accounts:
            for card in account.cards:
                if card.number == number and card.pin == pin:
                    print("You have successfully logged in!\n")
                    return True
        else:
            return False


class BankAccount:
    cards = []

    def __init__(self):
        self.card = BankCard()
        BankAccount.cards.append(self.card)


class BankCard:
    def __init__(self):
        self.pin = self.generate_pin()
        self.identifiers = self.generate_identifiers()
        self.number = self.number()
        print("Your card has been created")
        print("Your card number:\n" + self.number)
        print("Your card PIN:\n" + self.pin + "\n")

    @staticmethod
    def generate_pin():
        return ''.join(secrets.choice(string.digits) for i in range(4))

    @staticmethod
    def generate_identifiers():
        number = dict()
        number["IIN"] = '400000'
        number["Account Identifier"] = ''.join(secrets.choice(string.digits) for i in range(9))
        number["Checksum"] = ''.join(secrets.choice(string.digits) for i in range(1))
        return number

    def number(self):
        return str(self.identifiers["IIN"] +
                   self.identifiers["Account Identifier"] +
                   self.identifiers["Checksum"])


bank = Bank()
bank.menu()
