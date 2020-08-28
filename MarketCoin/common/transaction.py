#Import statements
from datetime import datetime
import hashlib
import json

#Transaction object declaration
class Transaction:
    def __init__(self, creation_stamp, recipient, sender, amount):
        self.creation_stamp = creation_stamp
        self.formatted_stamp = creation_stamp.strftime("%m/%d/%Y, %H:%M:%S")
        self.participants = [recipient, sender]
        self.amount = amount
        self.json_data = self.json_obj()
    
    def json_dump(self):
        obj = json.dumps({
            "transaction_timestamp": self.formatted_stamp, 
            "recipient": self.participants[0],
            "sender": self.participants[1],
            "amount": self.amount
        }, indent=2)
        return obj

    #To handle lists of transactions, compile all information into one total json document
    #use delimiters to separate, then print in chronological order)

    def json_obj(self):
        obj = {
            "transaction_timestamp": self.formatted_stamp, 
            "recipient": self.participants[0],
            "sender": self.participants[1],
            "amount": self.amount
        }
        return obj

