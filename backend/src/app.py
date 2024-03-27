from flask import Flask
from dotenv import dotenv_values


env_values = dotenv_values()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env_values.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def root():
    return '<h1>Hello!</h1>'
