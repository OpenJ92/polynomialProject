print('enter __init__')

import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import numpy as np

server = Flask(__name__)
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)
db.session.configure(autoflush=False)
app = dash.Dash(__name__, server = server, url_base_pathname = '/dashboard')

# from dashboard_views.dashboard import app
# import polynomial.routes
