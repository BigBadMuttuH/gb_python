from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def route():
    return 'Hi'


@app.route('/index/')
def index():
    context = dict(name='Anton')
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
