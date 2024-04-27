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


@app.cli.command('edit-user')
def edit_users():
    user = User.query.filter_by(username='John').first()
    user.email = 'john_new_mail@example.com'
    db.session.commit()
    print(f'{user.username} edit in DB!')


@app.cli.command('delete-user')
def delete_users():
    user = User.query.filter_by(username='John').first()
    db.session.delete(user)
    db.session.commit()
    print(f'{user.username} delete in DB!')


if __name__ == '__main__':
    app.run(debug=True)

# pwsh Flask add-user
# pwsh Flask edit-user
