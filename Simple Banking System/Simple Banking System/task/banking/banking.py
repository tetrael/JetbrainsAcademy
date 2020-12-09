import sqlite3
from sqlite3 import Error
from Bank import Bank


try:
    db_conn = sqlite3.connect('card.s3db')
    cursor = db_conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS card(
                            id INTEGER primary key,
                            number TEXT NOT NULL,
                            pin TEXT NOT NULL,
                            balance INTEGER DEFAULT 0
                        );""")
    db_conn.commit()
    bank = Bank(db_conn)
    bank.menu()
except Error as e:
    print(e)
finally:
    db_conn.close()
