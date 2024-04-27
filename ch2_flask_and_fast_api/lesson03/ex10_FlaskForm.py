# pip install Flask-WTF
from flask import Flask
from flask_wtf import FlaskForm, CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'8c518f7a4b26d5c0e986a4f1c9664310653810f2a1beff2caf85777566a23475'
"""
Защита от атаки CSRF (Cross-Site Request Forgery)
Как создать секретный ключ
import secrets
pkey = secrets.token_hex()
print(pkey)
"""
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt  # отключает защиту от атаки
def my_form():
    pass
    return 'No CSRF protection in action'


if __name__ == '__main__':
    app.run(debug=True)
