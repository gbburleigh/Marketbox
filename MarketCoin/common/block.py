#Import statements
from datetime import datetime
import hashlib
import json

#Block object declaration
#Contain transaction history info and are connected by 
# sharing hashes between consecutive blocks
    #Fingerprint - transaction + previous fingerprint
class Block:
    def __init__(self, previous_hash, transaction_data):
        self.previous_hash = previous_hash
        self.transaction_data = transaction_data
        self.current_hash = self.create_hash("".join(previous_hash) + str(transaction_data.json_dump()))

    def create_hash(self, data):
        hash = hashlib.sha256(str(data).encode()).hexdigest()
        #print(hash)
        return hash

    def dump_hash(self):
        return self.current_hash

    def print_status(self):
        print('------------------------------------------------------')
        print('\n')
        print('[*] Associated Hash: ', self.current_hash)
        print('\n')
        self.transaction_data.print_info()
        print('\n')