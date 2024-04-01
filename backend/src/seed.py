from app import app, db


def load_questions():
    questions = [
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BNThlZjI0MTgtODMzOC00ZjI2LWI3MTktMGQ3Y2FlM2Y5MDYwXkEyXkFqcGdeQXVyMTIwMjY0NjQz._V1_.jpg', 
            'answer': 'Get a Clue'
        },
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BOTZlYzU4MzAtZWQzMi00MmI1LWIxMWYtZjYxZmYzZTQ4ZjE2XkEyXkFqcGdeQXVyNTg3Njg4ODI@._V1_.jpg', 
            'answer': 'Gotta Kick It Up!'
        },
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BM2ZhMzE0MWItYmRjZS00ODBjLTkyNDgtOGZjMzgxN2Q2NjAxXkEyXkFqcGdeQXVyMTIwMjY0NjQz._V1_.jpg', 
            'answer': 'Stuck in the Suburbs'
        },
    ]
    db.questions.insert_many(questions)


def run():
    with app.app_context():
        print('Deleting Questions...')
        db.questions.delete_many({})

        print('Loading Questions...')
        load_questions()


if __name__ == '__main__':
    run()
