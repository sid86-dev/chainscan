from web3 import Web3
from rich.console import Console
console = Console()

infura_url = 'https://mainnet.infura.io/v3/d4c32f2944e341359b174ed9591ed71b'
web3 = Web3(Web3.HTTPProvider(infura_url))

# data = web3.eth.get_transaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
data = web3.eth.get_block('latest')

if __name__ == "__main__":
	for i in data:
		print(i)