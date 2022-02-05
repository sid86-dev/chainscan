from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

# getting contract
abi = json.loads('[{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress("0x1Dd347b18308c96F8c0B5A786Bb2A79a56aDED26")


# calling func from contract
contract = web3.eth.contract(address=address, abi=abi)
r = contract.functions.greet().call()
print(r)

# transact data
tx_hash = contract.functions.setGreeting('HELLO THIS IS Not SID!').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Updated greeting: {contract.functions.greet().call()}')