from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

account1 = "0x43bE284Ec0b3e8C71D878AFd9ad5414AE33bd413"
account2 = "0x4da96869344E1ca6a023fFf657e154A104D47678"

private_key = "4cbc7c195042395e49bf2776cda4fc02446bfe3c1d6123d0bce24d1b42d3f04d"

# get the nonce
nonce = web3.eth.getTransactionCount(account1)

# build a transaction
tx = {
	'nonce':nonce,
	'to':account2,
	'value': web3.toWei(1, 'ether'),
	'gas': 200000,
	'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get transaction hash
print(web3.toHex(tx_hash))