from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_01 import LoginForm, RegForm, RegisterForm

app = Flask(__name__,
            template_folder='../templates')
app.config['SECRET_KEY'] = b'8c518f7a4b26d5c0e986a4f1c9664310653810f2a1beff2caf85777566a23475'
csrf = CSRFProtect(app)


@app.route('/')
def imdex():
    return 'Hello, World!'


@app.route('/reg/', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
