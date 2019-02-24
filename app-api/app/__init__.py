from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

current_counts = 0

@app.route('/ping')
def index():
  return 'pong'

@app.route('/counts', methods=['GET', 'PUT'])
def counts():
  global current_counts

  if request.method == 'PUT':
    request_body = request.get_json()
    current_counts = request_body.get('counts', 0)

  response = jsonify(counts=current_counts)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.errorhandler(404)
def not_found(error):
  return 'Not Found!'

if __name__ == "__main__":
  app.run()
