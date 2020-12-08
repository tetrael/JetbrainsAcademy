from .BankAccount import BankAccount


class Bank:
    def __init__(self):
        self.accounts = []
        self.menu_exit = False

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
        while not self.menu_exit:
            self.print_main_menu()
            menu_item = int(input())
            if menu_item == 1:
                self.accounts.append(BankAccount())
            elif menu_item == 2:
                if self.login():
                    while True:
                        self.print_login_menu()
                        menu_item = int(input())
                        if menu_item == 1:
                            print("Balance: 0\n")
                            pass
                        elif menu_item == 2:
                            print("You have successfully logged out!\n")
                            break
                        elif menu_item == 0:
                            self.menu_exit = True
                            print("Bye!")
                            break
                else:
                    print("Wrong card number or PIN!\n")
            elif menu_item == 0 or self.menu_exit:
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