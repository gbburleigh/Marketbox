#Import statements
from datetime import datetime
from block import Block
from transaction import Transaction
from transaction_list import TransactionList
from util import *
import hashlib
import json

#Blockchain object declaration
class Blockchain:
    def __init__(self):
        self.genesis_block = self.create_genesis_block()
        self.blockchain = []
        self.hash_list = []
        self.pending_transactions = []
        self.failures = None
        self.transaction_list = TransactionList()
        self.transactions_verified = False
        self.blockchain.append(self.genesis_block)
        self.init_time = datetime.now()
        self.count = 0

    def create_genesis_block(self):
        #Ideally these parameters should be kept in .env file and changed automatically to improve
        #cryptographic strength of genesis block hashs
        transaction = Transaction(
            datetime.now(),
            "genesis_recipient",
            "genesis_sender",
            "0"
        )
        genesis_block = Block("genesis_block_message", "", 0)
        genesis_block.mine_block(1)
        return genesis_block

    #Adds a block object to the top of the blockchain
    #Requires verification that all transaction data is present
    #in object cache before adding to blockchain
    #Instantiates block object from transaction data and hash of top block
    
    def handle_transaction(self, transaction, bundling=False, difficulty=3):
        printPurple('[###] Handling Transaction')
        if bundling is True:
            self.transaction_list.add_transaction(transaction, bundling=True)
        else:
            self.transaction_list.add_transaction(transaction)

        # printRed('\n[DBG] DEBUG INFO\n')
        # printRed('-[DBG] Added transaction to list')
        # printRed('--[DBG] Top block hash: ', self.get_last_block().current_hash)
        block = Block(self.get_last_block().current_hash, 
            self.transaction_list.compile_json_dump(), self.count)
        # printRed('--[DBG] Instantiated block w/ hash: ', block.current_hash)
        self.count += 1
        self.hash_list.append(block.current_hash)
        block.mine_block(3)
        self = block.verify_transaction_data(self, return_failures=True)
        self.blockchain.append(block)
        return self
        
    def extract_block(self, idx):
        return self.blockchain[idx]

    def pull_fresh_hashes(self):
        self.transaction_list.hash_list = self.hash_list

    def purge_block(self, idx):
        self.blockchain.pop(idx)

    def get_last_block(self):
        return self.blockchain[-1]

    def get_first_block(self):
        return self.blockchain[0]

    def get_next_block(self, idx):
        return self.blockchain[idx+1]

    def stage_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def print_blockchain_status(self):
        printYellow(self.transaction_list.compile_json_dump())
        if self.transactions_verified is True:
            printGreen('[$$$] Successfully mined blocks with all transactions verified')
        else:
            printRed('[!!!] Transaction verification failed at some point')

