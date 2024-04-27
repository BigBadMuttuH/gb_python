from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return 'Hi'


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}!'
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
