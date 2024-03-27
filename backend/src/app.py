import random

from flask import Flask
from flask_migrate import Migrate
from dotenv import dotenv_values

from models import db, Card


env_values = dotenv_values()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env_values.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)


@app.route('/')
def root():
    return '<h1>Hello!</h1>'

@app.route('/cards')
def all_cards():
    return [c.to_dict() for c in Card.query.all()], 200

@app.route('/cards/<int:id>')
def card_by_id(id):
    card = Card.query.filter(Card.id == id).first()

    if not card:
        return {'error': 'card not found'}, 404
    
    return card.to_dict(), 200

@app.route('/cards/random')
def random_card():
    cards = Card.query.all()
    card = random.choice(cards)
    return card.to_dict(), 200
