import string
import secrets


class Card:
    def __init__(self, number=None, pin=None):
        self.pin = self.generate_pin() if pin is None else pin
        self.identifiers = self.generate_identifiers() if number is None else None
        self.number = self.card_number() if number is None else number
        print("\nYour card has been created")
        print("Your card number:\n" + self.number)
        print("Your card PIN:\n" + self.pin + "\n")

    @staticmethod
    def generate_pin():
        return ''.join(secrets.choice(string.digits) for _ in range(4))

    def generate_identifiers(self):
        self.number = dict()
        self.number["IIN"] = '400000'
        self.number["Account Identifier"] = ''.join(secrets.choice(string.digits) for _ in range(9))
        self.number["Checksum"] = self.calculate_checksum(str(self.number["IIN"]
                                                              + self.number["Account Identifier"]))
        return self.number

    def card_number(self):
        return str(self.identifiers["IIN"] +
                   self.identifiers["Account Identifier"] +
                   self.identifiers["Checksum"])

    @staticmethod
    def calculate_checksum(card_number):
        evens = list(int(_) for _ in card_number[1::2])
        odds = list(int(_) * 2 for _ in card_number[::2])
        odds = [x - 9 if x > 9 else x for x in odds]
        checksum = sum(evens) + sum(odds)
        for x in range(10):
            if (checksum + x) % 10 == 0:
                return str(x)

    def check_card_number(self, card_number):
        card_number = list(card_number)
        current_checksum = int(card_number[-1])
        del card_number[-1]
        calculated_checksum = int(self.calculate_checksum(card_number))
        return True if calculated_checksum == current_checksum else False
