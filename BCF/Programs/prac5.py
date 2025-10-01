from hashlib import sha256
import time

class Block:
    def __init__(self, timestamp, data, previousHash=' '):
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        return sha256(
            (str(self.timestamp) + str(self.data) + str(self.previousHash)).encode()
        ).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesis()]

    def createGenesis(self):
        return Block(time.ctime(), "Genesis Block", "00000")

    def mineBlock(self, data):
        node = Block(time.ctime(), data, self.chain[-1].hash)
        # mining a new block to the blockchain
        self.chain.append(node)

    def printBlockchain(self):
        for i in range(len(self.chain)):
            print("\n----- Block", i, "---------")
            print("Timestamp     :", self.chain[i].timestamp)
            print("Data          :", self.chain[i].data)
            print("Previous Hash :", self.chain[i].previousHash)
            print("Hash          :", self.chain[i].hash)


# Demo
CEVcoin = Blockchain()
data = input("Enter transaction data: ")

print("\n\n----> Mining New Block -->")
CEVcoin.mineBlock(data)
print("\n\n----> New Block mined successfully -->")
CEVcoin.printBlockchain()
