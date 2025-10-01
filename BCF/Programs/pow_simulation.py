import hashlib
import time

class Block:
    """
    Represents a single block in our blockchain.
    """
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # The nonce is the number we change to find a valid hash[cite: 11, 26].
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the SHA-256 hash of the block's contents.
        """
        # The block data is combined into a single string.
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        # The hash function is applied to the combined data[cite: 11].
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Manages the chain of blocks and the PoW consensus mechanism.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        # The difficulty determines how many leading zeros are required for a valid hash[cite: 11].
        self.difficulty = 4

    def create_genesis_block(self):
        """
        Creates the very first block in the chain.
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Returns the most recent block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, block):
        """
        Implements the Proof of Work algorithm.
        It finds a nonce that results in a hash with the required number of leading zeros.
        """
        # The target is a string of zeros with a length equal to the difficulty.
        target = '0' * self.difficulty
        
        # This loop represents the "mining" process.
        # It continuously adjusts the nonce and re-hashes until a valid hash is found[cite: 28].
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.calculate_hash()
        
        print(f"Block Mined! Nonce: {block.nonce}")
        return block

    def add_block(self, new_block):
        """
        Adds a new block to the chain after completing the proof of work.
        """
        new_block.previous_hash = self.get_latest_block().hash
        # The new block is passed to the proof_of_work function to be mined.
        mined_block = self.proof_of_work(new_block)
        self.chain.append(mined_block)

    def is_chain_valid(self):
        """
        Verifies the integrity of the blockchain.
        This demonstrates that verification is easy.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the block's hash is still valid.
            if current_block.hash != current_block.calculate_hash():
                print("Current hashes not equal")
                return False

            # Check if the block points correctly to the previous block's hash.
            if current_block.previous_hash != previous_block.hash:
                print("Previous hashes not equal")
                return False
        return True

# --- Main execution ---
if __name__ == "__main__":
    # Create a new blockchain instance.
    my_blockchain = Blockchain()

    # Add a few blocks to the chain.
    print("Mining block 1...")
    my_blockchain.add_block(Block(1, time.time(), {"sender": "Alice", "receiver": "Bob", "amount": 10}))
    
    print("\nMining block 2...")
    my_blockchain.add_block(Block(2, time.time(), {"sender": "Bob", "receiver": "Charlie", "amount": 5}))

    # Print the blockchain contents.
    print("\n--- Blockchain is valid:", my_blockchain.is_chain_valid(), "---\n")
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}\n")