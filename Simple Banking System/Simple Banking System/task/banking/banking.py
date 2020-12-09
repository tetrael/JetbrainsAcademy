from Bank import *
import sqlite3


# Only for passing test, all logic is in Database class
db_connection = sqlite3.connect('card.s3db')
cursor = db_connection.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS card(
                            id INTEGER primary key,
                            number TEXT NOT NULL,
                            pin TEXT NOT NULL,
                            balance INTEGER DEFAULT 0
                        );""")
bank = Bank()
bank.menu()
