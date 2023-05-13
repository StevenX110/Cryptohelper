import hashlib
import datetime as date

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = date.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print()

blockchain = Blockchain()

# Добавление новых блоков в блокчейн
blockchain.add_block("First block in blockchain")
blockchain.add_block("Second block in blockchain")
blockchain.add_block("Third block in blockchain")

blockchain.print_chain()
