import string
import secrets


class BankCard:
    def __init__(self):
        self.pin = self.generate_pin()
        self.identifiers = self.generate_identifiers()
        self.number = self.number()
        print("Your card has been created")
        print("Your card number:\n" + self.number)
        print("Your card PIN:\n" + self.pin + "\n")

    @staticmethod
    def generate_pin():
        return ''.join(secrets.choice(string.digits) for i in range(4))

    @staticmethod
    def generate_identifiers():
        number = dict()
        number["IIN"] = '400000'
        number["Account Identifier"] = ''.join(secrets.choice(string.digits) for i in range(9))
        number["Checksum"] = ''.join(secrets.choice(string.digits) for i in range(1))
        return number

    def number(self):
        return str(self.identifiers["IIN"] +
                   self.identifiers["Account Identifier"] +
                   self.identifiers["Checksum"])
