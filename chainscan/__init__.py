from flask import Flask
from .api.routes import api
from .auth.routes import auth
from .views import main
from .extensions import db


def create_app(config_file='settings.py'):
	app = Flask(__name__)
	
	app.config.from_pyfile(config_file)

	db.init_app(app)
	# register blueprint
	app.register_blueprint(api)
	app.register_blueprint(auth)
	app.register_blueprint(main)

	return app

