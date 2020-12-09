from BankCard import BankCard
from Database import Database


class BankAccount:
    def __init__(self):
        self.card = BankCard()
        self.cards = []
        self.cards.append(self.card)
        self.db = Database()
        self.db.insert_card_to_database(self.card)
