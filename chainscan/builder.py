from .settings import*
from web3 import Web3
from hexbytes import HexBytes
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)


web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def latestBlockData():
	data = web3.eth.get_block('latest')
	res = {}
	transactions = data['transactions']
	for key in data:
		value = data[key]
		try:
			value = value.hex()
		except:
			pass
		finally:
			res[key] = str(value)
		if key == 'transactions':
			l = [transaction.hex() for transaction in transactions]
			res['transactions'] = l
	return res


def sortedblockData(blocknum):
	blockData = web3.eth.getBlock(int(blocknum))
	res = {}

	l = ['number','hash']
	for key in blockData:
		if key in l:
			try:
				res[key] = blockData[key].hex()
			except:
				res[key] = blockData[key]
	return res 

def allblockData(blocknum):
	blockData = web3.eth.getBlock(int(blocknum))
	res = {}
	transactions = blockData['transactions']
	for key in blockData:
		if key != 'logsBloom':
			value = blockData[key]
			try:
				value = value.hex()
			except:
				pass
			finally:
				res[key] = value
			if key == 'transactions':
				l = [transaction.hex() for transaction in transactions]
				res['transactions'] = l
	return res 


def lastBlocksData(num):
	latest = web3.eth.blockNumber
	blocks = []
	names = [f"data{i}" for i in range(0,num)] 
	for i in range(0,num):
		n = latest-i
		names[i] = pool.apply_async(sortedblockData, (str(n),))

	for i in range(0, num):
		return_val = names[i].get()
		blocks.append(return_val)

	return blocks