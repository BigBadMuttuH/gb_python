from flask import Flask, render_template
from lesson03.models03 import db, User

app = Flask(__name__,
            template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/app.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/data/')
def data():
    return 'Your data'


@app.route('/users/')
def get_all_users():
    users = User.query.all()
    context = {
        'users': users
    }
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
