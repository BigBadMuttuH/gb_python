from flask import Flask
from lesson03.models03 import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Initialized the database.')


@app.cli.command('add-user')
def add_user():
    user = User(username='John', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print(f'{user.username} add in DB!')


if __name__ == '__main__':
    app.run(debug=True)

# pwsh Flask add-user
