from Card import Card
import sqlite3


class Bank:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = self.db_conn.cursor()
        self.menu_exit = False
        self.selected_card = None  # For login purpose

    @staticmethod
    def print_main_menu():
        print("\n1. Create an account")
        print("2. Log into account")
        print("3. Show database")
        print("0. Exit\n")

    @staticmethod
    def print_login_menu():
        print("\n1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit\n")

    def menu(self):
        while not self.menu_exit:
            self.print_main_menu()
            menu_item = int(input())
            if menu_item == 1:
                self.insert_card()
            elif menu_item == 2:
                if self.login():
                    while True:
                        self.print_login_menu()
                        menu_item = int(input())
                        if menu_item == 1:
                            print(f"Balance: {self.check_current_balance()}\n")
                        elif menu_item == 2:
                            self.increase_balance(int(input("Enter income:\n")))
                            print("Income was added!\n")
                        elif menu_item == 3:
                            self.do_transfer(input("Enter card number:\n"))
                        elif menu_item == 4:
                            self.close_account()
                            print("The account has been closed!\n")
                            break
                        elif menu_item == 5:
                            self.selected_card = None
                            print("You have successfully logged out!")
                            break
                        elif menu_item == 0:
                            self.menu_exit = True
                            print("Bye!")
                            break
                else:
                    print("Wrong card number or PIN!")
            elif menu_item == 3:
                # self.insert_card('3000003972196503','0000')  # for testing purposes
                self.cursor.execute("SELECT * FROM card")
                for row in self.cursor:
                    print(f"ID: {row[0]} No.: {row[1]} PIN: {row[2]} Balance: {row[3]}")
            elif menu_item == 0 or self.menu_exit:
                print("Bye!")
                break

    def login(self):
        number = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")

        self.cursor.execute("SELECT * FROM card")
        cards = self.cursor.fetchall()

        for card in cards:
                if card[1] == number and card[2] == pin:
                    self.selected_card = (card[1], card[2])
                    print("You have successfully logged in!\n")
                    return True
        else:
            return False

    def insert_card(self, number=None, pin=None):
        card = Card(number, pin)
        sql_query = f"INSERT INTO card (number, pin) VALUES( '" \
                    + card.number + "','" + card.pin + "');"
        self.cursor.execute(sql_query)
        self.db_conn.commit()

    def check_current_balance(self, card_number=None):
        sql_query = f"""SELECT * FROM card 
                        WHERE number = {self.selected_card[0] if card_number is None else card_number}"""
        self.cursor.execute(sql_query)
        balance = self.cursor.fetchone()
        return balance[3]

    def increase_balance(self, income, card_to=None):
        balance = int(self.check_current_balance(card_to))
        sql_query = f"""UPDATE card 
                        SET balance = {balance + income}
                        WHERE number = {self.selected_card[0] if card_to is None else card_to}"""
        self.cursor.execute(sql_query)
        self.db_conn.commit()

    def decrease_balance(self, outcome):
        balance = int(self.check_current_balance())
        sql_query = f"""UPDATE card 
                        SET balance = {balance - outcome}
                        WHERE number = {self.selected_card[0]}"""
        self.cursor.execute(sql_query)
        self.db_conn.commit()

    def is_card_in_database(self, card_number):
        sql_query = f"SELECT * FROM card WHERE number = {card_number}"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchone()
        return False if result is None or result[1] != card_number else True

    def do_transfer(self, card_to):
        if Card.check_card_number(card_to):  # Check is card number pass Luhn algorithm
            if self.is_card_in_database(card_to):
                amount_to_transfer = int(input("Enter how much money you want to transfer:\n"))
                if self.check_current_balance() >= amount_to_transfer:
                    self.decrease_balance(amount_to_transfer)
                    self.increase_balance(amount_to_transfer, card_to)
                    print("Success!")
                else:
                    print("Not enough money!")
            else:
                print("Such a card does not exist.")
        else:
            print("Probably you made a mistake in the card number. Please try again!")

    def close_account(self):
        sql_query = f"""DELETE FROM card 
                        WHERE number = {self.selected_card[0]}"""
        self.cursor.execute(sql_query)
        self.db_conn.commit()
