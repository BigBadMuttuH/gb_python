from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return 'Hi'


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        # фильтруем имя файла
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), app.static_folder, file_name))
        return f'File {file_name} uploaded'
    return render_template('upload-file.html')


if __name__ == '__main__':
    app.run(debug=True)
