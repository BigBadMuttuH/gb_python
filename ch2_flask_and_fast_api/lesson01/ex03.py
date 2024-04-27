from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'<h1>Hello, {name.capitalize()}!</h1>'


@app.route('/file/<path:filename>')
def send_file(filename):
    print(type(filename))
    return f'<h1>Путь до файла: "{filename}"</h1>'


@app.route('/number/<float:num>')
def numbers(num):
    print(type(num))
    return f'<h1>Передано число {num}</h1>'


@app.route('/<int:a>/<int:b>')
def sum_numbers(a, b):
    return f'<h2> Сумма чисел = {a + b}</h2>'


@app.route('/text/<string:text>')
def text_len(text):
    return f'<h1> {len(text)} </h1>'


if __name__ == '__main__':
    app.run(debug=True)
