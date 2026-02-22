from app import create_app

app = create_app('development')

if __name__ == "__main__":
    app.run()

from app import create_app, db

app = create_app('development')

with app.app_context():
    db.create_all()  