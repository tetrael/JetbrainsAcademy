from .BankCard import BankCard


class BankAccount:
    cards = []

    def __init__(self):
        self.card = BankCard()
        BankAccount.cards.append(self.card)