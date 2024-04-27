from flask import Flask, request

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок. <br>'
    return f'{text} {request.args}'


if __name__ == '__main__':
    app.run()