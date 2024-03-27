from app import app
from models import db, Card


def load_cards():
    cards = [
        Card(
            img_url='https://m.media-amazon.com/images/M/MV5BNThlZjI0MTgtODMzOC00ZjI2LWI3MTktMGQ3Y2FlM2Y5MDYwXkEyXkFqcGdeQXVyMTIwMjY0NjQz._V1_.jpg', 
            answer='Get a Clue'
        ),
        Card(
            img_url='https://m.media-amazon.com/images/M/MV5BOTZlYzU4MzAtZWQzMi00MmI1LWIxMWYtZjYxZmYzZTQ4ZjE2XkEyXkFqcGdeQXVyNTg3Njg4ODI@._V1_.jpg', 
            answer='Gotta Kick It Up!'
        ),
        Card(
            img_url='https://m.media-amazon.com/images/M/MV5BM2ZhMzE0MWItYmRjZS00ODBjLTkyNDgtOGZjMzgxN2Q2NjAxXkEyXkFqcGdeQXVyMTIwMjY0NjQz._V1_.jpg', 
            answer='Stuck in the Suburbs'
        ),
    ]
    db.session.add_all(cards)
    db.session.commit()


def run():
    with app.app_context():
        print('Deleting data...')
        Card.query.delete()

        print('Loading cards...')
        load_cards()


if __name__ == '__main__':
    run()
