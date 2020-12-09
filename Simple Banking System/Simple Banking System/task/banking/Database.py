import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self):
        self.db_connection = None
        self.create_db_connection()
        self.create_table_for_cards()

    def __del__(self):
        self.db_connection.close()

    def create_db_connection(self):
        try:
            self.db_connection = sqlite3.connect('card.s3db')
        except Error as e:
            print(e)
        finally:
            self.db_connection.close()

    def create_table_for_cards(self):
        try:
            self.db_connection = sqlite3.connect('card.s3db')
            cursor = self.db_connection.cursor()
            sql_query = """ CREATE TABLE IF NOT EXISTS card(
                                        id INTEGER primary key,
                                        number TEXT NOT NULL,
                                        pin TEXT NOT NULL,
                                        balance INTEGER DEFAULT 0
                                    );"""
            cursor.execute(sql_query)
        except Error as e:
            print(e)
        finally:
            self.db_connection.close()

    def insert_card_to_database(self, card):
        try:
            self.db_connection = sqlite3.connect('card.s3db')
            cursor = self.db_connection.cursor()
            sql_query = "INSERT INTO card (number, pin) VALUES( " \
                        + card.number \
                        + ", " \
                        + card.pin \
                        + ");"
            cursor.execute(sql_query)
            self.db_connection.commit()
            cursor.execute("SELECT * FROM card")
            for row in cursor:
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print('\n')
        except Error as e:
            print(e)
        finally:
            self.db_connection.close()
