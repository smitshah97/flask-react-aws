# services/users/project/__init__.py


import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask import Blueprint, jsonify, request, redirect
import sys
import pandas as pd
import pymongo
import json
import io
import simplejson
from flask_request_params import bind_request_params
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from .feature_selector import FeatureSelector
from sklearn.feature_selection import RFE
import numpy as np
from sklearn.linear_model import LassoCV
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectFpr, chi2
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_poisson_deviance
from sklearn.metrics import mean_gamma_deviance
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import jaccard_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import nltk
import re
from nltk.stem.snowball import SnowballStemmer
from kmodes.kmodes import KModes
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
