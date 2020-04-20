# services/users/project/api/__init__.py
from flask import Flask,Blueprint, jsonify, request, redirect
import sys
import json
import io
import simplejson
from flask_request_params import bind_request_params


from flask_cors import CORS, cross_origin

from flask_restx import Api

from project.api.auth import auth_namespace
from project.api.ping import ping_namespace
from project.api.users.views import users_namespace



main = Flask(__name__)
main.before_request(bind_request_params)

cors = CORS(main)
main.config['CORS_HEADERS'] = 'Content-Type'
api = Api(version="1.0", title="Users API", doc="/doc/")
@main.route('/sampletest')
def sampleawstest():
   
    return jsonify({'movies' : "SAMPLE TEST"})

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(auth_namespace, path="/auth")
