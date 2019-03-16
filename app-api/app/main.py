from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


database_host = os.environ['DATABASE_HOST']
database_user = os.environ['DATABASE_USER']
database_password = os.environ['DATABASE_PASSWORD']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{database_user}:{database_password}@{database_host}/app-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
CORS(app)

from .models import Counter

@app.route('/counts', methods=['GET', 'PUT'])
def counts():
  counter = Counter.query.first()

  if counter == None:
    new_counter = Counter(counts=0)
    db.session.add(new_counter)
    db.session.commit()
    response = jsonify(counts=0)

  if request.method == 'PUT':
    request_body = request.get_json()
    new_counts = request_body.get('counts', 0)
    counter.counts = new_counts
    db.session.commit()
    print(request_body)
    response = jsonify(counts=new_counts)

  if request.method == 'GET':
    response = jsonify(counts=counter.counts)

  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.errorhandler(404)
def not_found(error):
  return 'Not Found!'
