from flask import Flask
from lesson03.models03 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return f'<h1>Hello, World!</h1>'


@app.cli.command("init-db")
def init_db():
    # db.drop_all()
    db.create_all()
    # db.session.commit()
    print('Database initialized')


if __name__ == '__main__':
    app.run(debug=True)
# Flask init-db
# Если так запустить, то получим ошибку
# Error: Failed to find Flask application or factory in module 'wsgi'. Use 'wsgi:name' to specify one.
# Чтобы это исправить, нужно импортировать нашу модуль в wsgi.py
