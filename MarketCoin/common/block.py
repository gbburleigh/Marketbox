#Import statements
from datetime import datetime
import hashlib
import json
import sys
from util import *

#Block object declaration
#Contain transaction history info and are connected by 
# sharing hashes between consecutive blocks
    #Fingerprint - transaction + previous fingerprint
class Block:
    def __init__(self, previous_hash, transaction_data, index):
        self.previous_hash = previous_hash
        self.transaction_data = transaction_data
        self.hash_payload = previous_hash + transaction_data
        self.current_hash = self.create_hash(self.hash_payload)
        self.index = index
        self.validity = False
        self.mined = False
        self.checksum = None
        self.nonce = 0

    def create_hash(self, data):
        hash = hashlib.sha256(str(data).encode()).hexdigest()
        return hash

    #broken, fix this
    def dump_hash(self):
        return self.current_hash

    def mine_block(self, difficulty):
        zeros = ['0'] * difficulty
        #printYellow('[*] Began Mining', [zeros, [num for num in self.current_hash[0:difficulty]], self.current_hash])
        while [num for num in self.current_hash[0:difficulty]] != zeros:
            self.nonce += 1
            self.current_hash = self.create_hash(self.hash_payload + str(self.nonce))
            # printCyan('[*] Iter: ', self.nonce)
            # printCyan(self.current_hash)

        #printGreen('[$$$] Successfully mined with difficulty: ', difficulty)
        #printGreen('[$$$] A coin has been added to the associate wallet')
        #printGreen('[$$$] This block is now valid to use in any transaction.')
        self.mined = True
        return self
        
    def verify_transaction_data(self, bc, return_failures=False):
        printPurple('\n[###] Verifying Transaction Data')
        failures = {}
        if bc.count > 1:
            prev = bc.get_first_block()
            broken = False
            for i in range(1, bc.count-1):
                #printRed('Trying to access blockchain at index: ', [i, len(bc.blockchain)])
                curr = bc.blockchain[i]
                #printCyan([curr.current_hash, curr.create_hash(curr.hash_payload + str(curr.nonce))])
                if curr.current_hash != curr.create_hash(curr.hash_payload + str(curr.nonce)):
                    printRed('[!!!] Error verifying block at position: ', i)
                    printRed('- [!!!] Block hash record inconsistent with created hash')
                    failures[i] = [curr.current_hash, curr.create_hash(curr.hash_payload + str(curr.nonce))]
                    broken = True
                elif curr.previous_hash != prev.current_hash:
                    printRed('[!!!] Error verifying block at position: ', i)
                    printRed("- [!!!] Previous hash didn't match previous block record")
                    failures[i] = [curr.previous_hash, prev.current_hash]
                    broken = True
                prev = curr
            if broken is False:
                printGreen('[***] Block verified transactions successfully')
                bc.transactions_verified = True
                self.validity = True
        else:
            printLightPurple('[***] Blockchain requires additional blocks before verification')

        if return_failures is True:
            bc.failures = failures

        return bc

    def check_block_integrity(self):
        if self.validity is True and self.mined is True:
            printGreen('[***] Block integrity verified.')
            return True
        else:
            printRed('[!!!] Error verifying block integrity: ', [
                    self.mined,
                    self.validity
                ])

            return False

            
