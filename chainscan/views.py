from flask import Blueprint, jsonify, render_template
from .builder import *

main = Blueprint('main', __name__)

@main.get('/')
def index():
	last_ten_blocks = lastBlocksData(10)
	return render_template('/Client/index.html', lastTenBlocks=last_ten_blocks)

@main.get('/blockData/<int:blocknumber>')
def getblockdata(blocknumber):
	block_data = allblockData(blocknumber)
	return render_template('/Client/blockDetails.html', blockData=block_data)

