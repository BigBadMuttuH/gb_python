from flask import Flask, url_for, redirect

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/redirect')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external')
def redirect_to_external():
    return redirect('https://google.com')


@app.route('/redirect/<name>/')
def redirect_to_hello(name):
    """
    Route decorator to redirect to the hello function with the provided name parameter.

    Parameters:
    name (str): The name used in the redirect URL.

    Returns:
    werkzeug.wrappers.response.Response: A response object that redirects to the hello function with the provided name.
    """
    return redirect(url_for('hello', name=name))


@app.route('/hello/<name>/')
def hello(name):
    return f'<h1>Hello, {name}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
