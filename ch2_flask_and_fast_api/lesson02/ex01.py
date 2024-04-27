from flask import Flask, send_from_directory

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return 'Введите путь к файлу в адресной строке.'


@app.route('/get-file/<file>')
def get_file(file):
    """Возвращает файл из папки static."""
    # return send_from_directory(app.static_folder, file)
    # так возвращается как отдельный файл, который можно скачать
    return send_from_directory(app.static_folder, file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
