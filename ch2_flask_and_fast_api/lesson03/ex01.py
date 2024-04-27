from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@server/db_name' app.config[
# 'SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@server/db_name'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Отключает функцию отслеживания изменений объектов в Flask-SQLAlchemy.
# По умолчанию SQLAlchemy сообщает приложению каждый раз,
# когда изменяется состояние объекта в базе данных. Это может быть полезным для отладки, но это также замедляет
# работу приложения и потребляет дополнительную память, особенно при большом объеме транзакций. Установка этого
# значения в False повышает производительность и рекомендуется для большинства проектов.

db = SQLAlchemy(app)


@app.route('/')
def index():
    return '<h1>Hi</h1>'


if __name__ == '__main__':
    app.run(debug=True)
