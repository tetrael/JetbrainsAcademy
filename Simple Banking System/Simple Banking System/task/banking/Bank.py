from BankAccount import BankAccount
import sqlite3


class Bank:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = self.db_conn.cursor()
        self.menu_exit = False
        self.chosen_account = None # For login purpose

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
                account = BankAccount()
                sql_query = f"INSERT INTO card (number, pin) VALUES( " \
                                + account.number + "," + account.pin + ");"
                self.cursor.execute(sql_query)
                self.db_conn.commit()
            elif menu_item == 2:
                if self.login():
                    while True:
                        self.print_login_menu()
                        menu_item = int(input())
                        if menu_item == 1:
                            sql_query = f"""SELECT * FROM card 
                                            WHERE number = {self.chosen_account[0]} 
                                            AND pin = {self.chosen_account[1]}"""
                            self.cursor.execute(sql_query)
                            balance = self.cursor.fetchone()
                            print(f"Balance: {balance[3]}\n")
                        elif menu_item == 2:
                            income = int(input("Enter income:"))
                            sql_query = f"""UPDATE card 
                                            SET balance = {income}
                                            WHERE number = {self.chosen_account[0]}
                                            AND pin = {self.chosen_account[1]}"""2
                            self.cursor.execute(sql_query)
                            self.db_conn.commit()
                            print("Income was added!\n")
                        elif menu_item == 3:
                            print("Not implemented yet!\n")
                            pass
                        elif menu_item == 4:
                            print("Not implemented yet!\n")
                            pass
                        elif menu_item == 5:
                            self.chosen_account = None
                            print("You have successfully logged out!\n")
                            break
                        elif menu_item == 0:
                            self.menu_exit = True
                            print("Bye!")
                            break
                else:
                    print("Wrong card number or PIN!\n")
            elif menu_item == 3:
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
        accounts = self.cursor.fetchall()

        for account in accounts:
                if account[1] == number and account[2] == pin:
                    self.chosen_account = (account[1], account[2])
                    print("You have successfully logged in!\n")
                    return True
        else:
            return False
