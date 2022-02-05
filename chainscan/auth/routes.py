from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/v1/auth')

@auth.post('/login')
def login():
	return "Hello world Auth"