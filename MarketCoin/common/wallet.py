#Import statements
from datetime import datetime
from block import Block
from transaction import Transaction
from transaction_list import TransactionList
from util import *
import hashlib
import json

class Wallet:
    def __init__(self, user_data):
        self.coins = []
        self.user_data_json = user_data
        self.user_fields = []
        self.nonce = 0
        self.address = self.generate_address()[:24]
        self.balance = 0

    def find_balance(self, tl):
        bal = 0
        for transaction in tl:
            if transaction.participants[0] is self.address:
                bal += transaction.amount

        self.balance = bal
        return self

    def verify_coin_integrity(self):
        pass

    def generate_address(self):
        d = json.loads(self.user_data_json)
        s = str(self.nonce)
        for field in d.values():
            printLightGray('[-]', field)
            self.user_fields.append(field)
            s += str(field)

        hash = hashlib.sha256(s.encode()).hexdigest()
        return hash

if __name__ == "__main__":
    w = Wallet('{ "username": "test_username", "password": "test-password", \
        "email": "test-email"}')
    print(w.address)
