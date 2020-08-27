#Import statements
from datetime import datetime
from block import Block
from transaction import Transaction
import hashlib
import json

#Blockchain object declaration
class Blockchain:
    def __init__(self):
        self.genesis_block = self.create_genesis_block()
        self.blockchain = []
        self.blockchain.append(self.genesis_block)
        self.init_time = datetime.now()

    def create_genesis_block(self):
        #Ideally these parameters should be kept in .env file and changed automatically to improve
        #cryptographic strength of genesis block hashs
        genesis_block = Block("genesis_block_message", Transaction(
            datetime.now(),
            "genesis_recipient",
            "genesis_sender",
            "0"
        ))
        return genesis_block

    def add_block(self, block):
        self.blockchain.append(block)
        return

    def extract_block(self, idx):
        return self.blockchain[idx]

    def purge_block(self, idx):
        self.blockchain.pop(idx)

    def get_last_block(self):
        return self.blockchain[-1]

    def get_first_block(self):
        return self.blockchain[0]

    def print_blockchain_status(self):
        for block in self.blockchain:
            block.print_status()

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block(Block(
        blockchain.get_first_block().dump_hash(), Transaction(
            datetime.now(),
            "recipient-test",
            "sender-test",
            "2.5"
        )
    ))

    blockchain.print_blockchain_status()