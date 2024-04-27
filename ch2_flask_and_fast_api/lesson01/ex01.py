from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"
    # можно возвращать только строку


# flask --app .\ex01\lesson_01.py run
if __name__ == '__main__':
    app.run()
