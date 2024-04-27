from flask import Flask
from lesson03.models02 import db


app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)


@app.route('/')
def index():
    return '<h1>Hi</h1>'


if __name__ == '__main__':
    app.run(debug=True)
