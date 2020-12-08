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
        print("0. Exit")

    @staticmethod
    def print_login_menu():
        print("1. Balance")
        print("2. Log out")
        print("0. Exit")

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
                            print("Balance: 0")
                            pass
                        elif menuitem == 2:
                            print("You have successfully logged out!")
                            break
                        elif menuitem == 0:
                            self.menuexit = True
                            print("Bye!")
                            break
                else:
                    print("Wrong card number or PIN!")
            elif menuitem == 0 or self.menuexit:
                print("Bye!")
                break

    def login(self):
        account = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")
        if account in self.accounts:
            return True
        else:
            return False


class BankAccount:
    accounts = []

    def __init__(self):
        self.card = BankCard()
        BankAccount.accounts.append(self.card)


class BankCard:
    def __init__(self):
        self.pin = self.generate_pin()
        self.number = self.generate_number()
        print("Your card has been created")
        print("Your card number:\n" + self.card_number())
        print("Your card PIN:\n" + self.pin)

    @staticmethod
    def generate_pin():
        return ''.join(secrets.choice(string.digits) for i in range(4))

    @staticmethod
    def generate_number():
        number = dict()
        number["IIN"] = '400000'
        number["Account Identifier"] = ''.join(secrets.choice(string.digits) for i in range(9))
        number["Checksum"] = ''.join(secrets.choice(string.digits) for i in range(1))
        return number

    def card_number(self):
        return str(self.number["IIN"] +
                   self.number["Account Identifier"] +
                   self.number["Checksum"])


bank = Bank()
bank.menu()
