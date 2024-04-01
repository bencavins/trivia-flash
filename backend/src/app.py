import random
import json

from flask import Flask
from flask_cors import CORS
from dotenv import dotenv_values
from pymongo import MongoClient
from bson import json_util

env_values = dotenv_values()
app = Flask(__name__)

client = MongoClient(env_values.get('MONGO_DB_URI'))
db = client.trivia

CORS(app)


@app.route('/')
def root():
    return '<h1>Hello!</h1>'

@app.route('/cards')
def all_cards():
    return [json.loads(json_util.dumps(record)) for record in db.questions.find()], 200

@app.route('/cards/random')
def random_card():
    record = random.choice(all_cards()[0])
    return record, 200
