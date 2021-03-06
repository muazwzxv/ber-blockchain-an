from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, transaction, time, prev_hash, nonce=0):
        self.index = index
        self.transaction = transaction
        self.time = time
        self.prev_hash = prev_hash
        self.nonce = nonce

    def compute_hash(self, block):
        # Returns the hash of the block contents

        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
