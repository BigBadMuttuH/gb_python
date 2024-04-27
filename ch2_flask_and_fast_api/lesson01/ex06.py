from flask import flash, jsonify, request, Flask, render_template

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static',
)


@app.route('/')
def route():
    return "Hello World!"


@app.route('/students')
def students():
    student_list = [
        {
            'name': 'Ivan',
            'age': 18,
            'gender': 'male'
        },
        {
            'name': 'Ron',
            'age': 19,
            'gender': 'male'
        },
        {
            'name': 'Anna',
            'age': 17,
            'gender': 'female'
        },
    ]
    context = {
        'students': student_list
    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
