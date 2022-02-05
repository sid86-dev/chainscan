from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/d4c32f2944e341359b174ed9591ed71b'

web3 = Web3(Web3.HTTPProvider(infura_url))

conn_status = web3.isConnected()
current_block = web3.eth.block_number

metamask_address = '0x8281D00277d2C903705c732aC14A3103ba15a1cd'

balance = web3.eth.getBalance(metamask_address)
ether = web3.fromWei(balance, 'ether')

print(f"Your current balance is {ether} ETH")