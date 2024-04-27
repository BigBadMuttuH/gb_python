from flask import Flask, jsonify, request

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="ru">
<h1>Привет, мир!!!!!</h1>
<p>Тут какой-то абзац. <br>Тут переход на новую строку.</br></p>
"""


@app.route('/')
def index_page():
    return 'Hi!'


@app.route('/text/')
def text_page():
    return html


if __name__ == '__main__':
    app.run(debug=True)
