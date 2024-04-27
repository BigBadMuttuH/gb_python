from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify
from lesson03.models03 import db, User, Post


app = Flask(__name__,
            template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/app.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/data/')
def data():
    return 'Your data'


@app.route('/users/')
def get_all_users():
    users = User.query.all()
    context = {
        'users': users
    }
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def get_user_by_name(username):
    users = User.query.filter(User.username == username).all()
    context = {
        'users': users
    }
    return render_template('users.html', **context)


@app.route('/post/author/<int:user_id>')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id,
              'title': post.title,
              'content': post.content,
              'created_at': post.created_at
              } for post in posts]
        )
    else:
        return jsonify({'error': 'Posts not found'}), 404


@app.route('/post/last-week')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify(
            [{'id': post.id,
              'title': post.title,
              'content': post.content,
              'created_at': post.created_at
              } for post in posts]
        )
    else:
        return jsonify({'error': 'Posts not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
