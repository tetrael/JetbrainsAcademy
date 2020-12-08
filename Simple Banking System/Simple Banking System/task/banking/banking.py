import string
import secrets


class Bank:
    def __init__(self):
        self.accounts = []

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
        self.print_main_menu()
        while True:
            menuitem = int(input())
            if menuitem == 1:
                self.accounts.append(BankAccount())
            elif menuitem == 2:
                pass
            elif menuitem == 0:
                break


class BankAccount:
    accounts = []

    def __init__(self):
        self.card = BankCard()
        BankAccount.accounts.append(self.card)

    @staticmethod
    def login():
        account = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")


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
