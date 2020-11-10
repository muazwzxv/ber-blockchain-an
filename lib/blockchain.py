from .block import Block
from flask import Flask, request
import requests


class Blockchain:

    # Rate of difficulty of our Proof of work algo
    level = 2

    def __init__(self):
        self.unconfirmed_transac = []
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        """
        Generates a genesis block and appends it to the chain
        index = 0
        previous hash = 0
        valid hash = 1
        """
        genesis = Block(0, [], 0, "0")
        genesis.hash = genesis.compute_hash(genesis)

        self.chain.append(genesis)

    @property
    def last_block(self):
        return self.chain[-1]

    def getFirstBlock(self):
        return self.chain[0]

    def add(self, block, proof):
        """
        Adds block to the chain after verified
        - Checks valid proof
        - Checks if the referred prev_hash in the block matches with latest block in the chain
        """

        prev_hash = self.last_block.hash

        if prev_hash != block.prev_hash:
            return False

        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        # Checks if block_hash is valid and satisfie the difficulty criteria
        return (
            block_hash.startswth("0" * Blockchain.level)
            and block_hash == block.compute_hash()
        )

    def proof_of_work(self, block):
        # Tries different vaue of nonce to get a hash that satisfies our level criteria
        # Once the proper nonce is found, the compute_hash based on the nonce that satisfie the condition
        # is returned

        block.nonce = 0
        compute_hash = block.compute_hash()
        while not compute_hash.startswith("0" * Blockchain.level):
            block.nonce += 1
            compute_hash = block.compute_hash()

        return compute_hash
