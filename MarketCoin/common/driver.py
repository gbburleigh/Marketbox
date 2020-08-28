#Import statements
from datetime import datetime
from block import Block
from transaction import Transaction
from blockchain import Blockchain
import hashlib
import json
from wallet import Wallet
from util import *
import random
import time

#Driver file for testing blockchain
#Eventually integrate this as a wrapper file to REST API for server to interact with

class Driver:
    def __init__(self, driver_mode="testing"):
        self.driver_mode = driver_mode

    def run(self):
        blockchain = Blockchain()
        
        t = Transaction(
                datetime.now(),
                "recipient-test",
                "sender-test",
                "2.5"
            )

        blockchain = blockchain.handle_transaction(t)

        # printCyan('[***] Transaction check', t.json_dump())
        # printPurple('[***] Produced transaction', blockchain.transaction_list.print_latest_entry())
        # printLightPurple('[***] Ensure JSON compilation/printing works: ')
        # printLightPurple(blockchain.transaction_list.compile_json_dump())

        blockchain.print_blockchain_status()

        

        t = Transaction(
            datetime.now(),
            "recipient-2",
            "sender-2",
            "5"
        )

        blockchain = blockchain.handle_transaction(t)
        blockchain.pull_fresh_hashes()
    
        printYellow(blockchain.transaction_list.compile_json_dump())

        return blockchain

    def run_node_generation(self):
        #Testing for generating many nodes at a time, first without bundling then with
        blockchain = Blockchain()
        wallet_list = []
        for i in range(25):
            obj = { 
                "username": "walletusername" + str(i), 
                "password": "walletpassword" + str(i), 
                "email": "walletemail" + str(i) + "@gmail.com" 
                }
            jsonobj = json.dumps(obj)
            w = Wallet(jsonobj)
            wallet_list.append(w)
        printLightGray('[----------] Wallet Init Complete')

        printLightGray('[---] Continue?')
        inp = input()

        for i in range(50):
            time = datetime.now()
            idx = random.sample(range(25), 2)
            recipient = wallet_list[idx[0]].address
            sender = wallet_list[idx[1]].address
            amount = random.randrange(0, 50)
            t = Transaction(
                time,
                recipient,
                sender,
                amount
            )
            blockchain.handle_transaction(t)

        bundle = []
        for j in range(50):
            time = datetime.now()
            idx = random.sample(range(25), 2)
            recipient = wallet_list[idx[0]].address
            sender = wallet_list[idx[1]].address
            amount = random.randrange(0, 50)
            t = Transaction(
                time,
                recipient,
                sender,
                amount
            )
            bundle.append(t)
            if ((j % 5) == 0):
                blockchain.handle_transaction(bundle, bundling=True)
                bundle = []

        blockchain.print_blockchain_status()

if __name__ == "__main__":
    Driver().run_node_generation()