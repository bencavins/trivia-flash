from app import app, db


def load_questions():
    questions = [
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BNThlZjI0MTgtODMzOC00ZjI2LWI3MTktMGQ3Y2FlM2Y5MDYwXkEyXkFqcGdeQXVyMTIwMjY0NjQz._V1_.jpg', 
            'answer': 'Get a Clue',
            'category': 'Movies',
            'subcategory': 'Disney Channel Original Movies',
        },
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BOTZlYzU4MzAtZWQzMi00MmI1LWIxMWYtZjYxZmYzZTQ4ZjE2XkEyXkFqcGdeQXVyNTg3Njg4ODI@._V1_.jpg', 
            'answer': 'Gotta Kick It Up!',
            'category': 'Movies',
            'subcategory': 'Disney Channel Original Movies',
        },
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BM2ZhMzE0MWItYmRjZS00ODBjLTkyNDgtOGZjMzgxN2Q2NjAxXkEyXkFqcGdeQXVyMTIwMjY0NjQz._V1_.jpg', 
            'answer': 'Stuck in the Suburbs',
            'category': 'Movies',
            'subcategory': 'Disney Channel Original Movies',
        },
        {
            'img_url': 'https://www.commonsensemedia.org/sites/default/files/styles/social_share_image/public/screenshots/csm-movie/jen2.jpg', 
            'answer': 'The Jennie Project',
            'category': 'Movies',
            'subcategory': 'Disney Channel Original Movies',
        },
        {
            'img_url': 'https://m.media-amazon.com/images/M/MV5BOTM4MTMwZWItNmZkYy00ZmE4LTkyMGYtZGRmOWQ1ZWYwZDNiXkEyXkFqcGdeQXVyODg0NTYwMjM@._V1_.jpg', 
            'answer': 'Cadet Kelly',
            'category': 'Movies',
            'subcategory': 'Disney Channel Original Movies',
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
