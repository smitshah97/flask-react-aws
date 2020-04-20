# services/users/project/__init__.py


import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask import Blueprint, jsonify, request, redirect

#from . import db 
#from .models import Movie
from flask_cors import cross_origin

# instantiate the extensions
db = SQLAlchemy()
cors = CORS()
bcrypt = Bcrypt()
admin = Admin(template_mode="bootstrap3")
main = Flask(__name__)
main.before_request(bind_request_params)

cors = CORS(main)
main.config['CORS_HEADERS'] = 'Content-Type'


@main.route('/sample', methods=['GET'])
def sampleawstest():
    
    return jsonify({'movies' : "SAMPLE TEST"})


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    bcrypt.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register api
    from project.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
