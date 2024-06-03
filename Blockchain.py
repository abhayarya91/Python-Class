from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().calculate_hash()
        new_block.index = self.get_latest_block().index + 1
        new_block.nonce = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block, difficulty=2):
        nonce = 0
        computed_hash = block.calculate_hash()
        while not computed_hash.startswith('0' * difficulty):
            nonce += 1
            block.nonce = nonce
            computed_hash = block.calculate_hash()
        return nonce

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.calculate_hash() != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.calculate_hash():
                return False
        return True

# Example usage
# if __name__ == "__main__":
#     blockchain = Blockchain()
#     blockchain.add_block(Block(1, time.time(), "Data 1", ""))
#     blockchain.add_block(Block(2, time.time(), "Data 2", ""))
    
#     print("Blockchain is valid:", blockchain.is_chain_valid())

#     # Tampering with data to simulate a Man-in-the-Middle attack
#     blockchain.chain[1].data = "Modified Data"

#     print("Blockchain is valid after tampering:", blockchain.is_chain_valid())
