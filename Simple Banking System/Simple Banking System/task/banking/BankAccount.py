import string
import secrets


class BankAccount:
    def __init__(self):
        self.pin = self.generate_pin()
        self.identifiers = self.generate_identifiers()
        self.number = self.card_number()
        print("Your card has been created")
        print("Your card number:\n" + self.number)
        print("Your card PIN:\n" + self.pin + "\n")

    @staticmethod
    def generate_pin():
        return ''.join(secrets.choice(string.digits) for i in range(4))

    def generate_identifiers(self):
        self.number = dict()
        self.number["IIN"] = '400000'
        self.number["Account Identifier"] = ''.join(secrets.choice(string.digits) for i in range(9))
        self.number["Checksum"] = self.checksum(str(self.number["IIN"]
                                                    + self.number["Account Identifier"]))
        return self.number

    def card_number(self):
        return str(self.identifiers["IIN"] +
                   self.identifiers["Account Identifier"] +
                   self.identifiers["Checksum"])

    @staticmethod
    def checksum(checksum):
        if len(checksum) > 15:
            del checksum[-1]

        evens = list(int(_) for _ in checksum[1::2])
        odds = list(int(_) * 2 for _ in checksum[::2])
        odds = [x - 9 if x > 9 else x for x in odds]

        checksum = sum(evens) + sum(odds)

        for x in range(10):
            if (checksum + x) % 10 == 0:
                return str(x)
