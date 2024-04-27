from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


@app.route('/')
def index():
    return f'<h1>Hello, World!</h1>'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        flash('Форма успешно отправлена', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
