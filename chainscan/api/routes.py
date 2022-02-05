from flask import Blueprint
from chainscan.builder import *

api = Blueprint('api', __name__, url_prefix='/api')

@api.get('/latestBlock')
def getLatestBlock():
	data = LatestBlockData()
	
	return data
