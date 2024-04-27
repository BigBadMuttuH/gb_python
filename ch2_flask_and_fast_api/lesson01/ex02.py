from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет мир!'


@app.route('/Николай/')  # имя функции дают такое же, как и путь для браузера
def get_user_nikolay():
    return 'Привет, Николай'


@app.route('/Иван/')
def get_user_ivan():
    return 'Привет, Иван!'


@app.route('/list/')
def get_user_list():
    return [_ for _ in range(1, 11)]


if __name__ == '__main__':
    app.run(debug=True)
