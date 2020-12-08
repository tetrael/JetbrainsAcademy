from BankCard import BankCard


class BankAccount:
    def __init__(self):
        self.card = BankCard()
        self.cards = []
        self.cards.append(self.card)
