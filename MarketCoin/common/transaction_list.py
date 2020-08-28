#Import statements
from datetime import datetime
import hashlib
import json
from util import *
from transaction import Transaction

#Transaction list object declaration
#This is purely a class to handle compiling JSON data
#   The blockchain will still handle transaction objects in
#   order to grow itself.
class TransactionList:
    def __init__(self, hash_list=None):
        self.transactions = []
        self.json_data = None
        self.hash_list = hash_list
        self.count = 0

    def add_transaction(self, transaction, bundling=False):
        if bundling is True:
            for t in transaction:
                self.transactions.append(t)
                self.count += 1
        else:
            self.transactions.append(transaction)
            self.count += 1

        return self

    def fetch_transaction(self, index):
        return self.transactions[index]

    def print_latest_entry(self):
        return json.dumps(self.transactions[-1].json_obj(), indent=2)

    def compile_json_data(self):
        s = ''
        idx = 0
        total_json = {}
        for t in self.transactions:
            #printYellow('[TransactionList] Got transaction: ', t.json_obj())
            # s += '\n'
            # s += t.json_dump()
            # s += '\n'
            if self.hash_list is None:
                total_json[idx] = t.json_obj()
                idx += 1
            else:
                total_json[self.hash_list[idx]] = t.json_obj()
                idx += 1

        #all_transactions = json.loads(s)
        self.json_data = total_json
        return total_json

    def compile_json_dump(self):
        self.compile_json_data()
        return json.dumps(self.json_data, indent=4)

if __name__ == "__main__":
    transaction1 = Transaction(
            datetime.now(),
            "genesis_recipient1",
            "genesis_sender1",
            "1"
        )
    transaction2 = Transaction(
            datetime.now(),
            "genesis_recipient2",
            "genesis_sender2",
            "2"
        )
    transaction3 = Transaction(
            datetime.now(),
            "genesis_recipient3",
            "genesis_sender3",
            "3"
        )

    t = TransactionList()
    t = t.add_transaction([
            transaction1, 
            transaction2, 
            transaction3],
            bundling=True)
    
    jsondata = t.compile_json_data()
    printRed(json.dumps(jsondata, indent=4))
