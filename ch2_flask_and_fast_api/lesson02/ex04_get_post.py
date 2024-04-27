from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return 'Hi'


@app.get('/submit/')
def submit_get():
    return render_template('upload.html')


@app.post('/submit/')
def submit_post():
    name = request.form.get('name')
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
