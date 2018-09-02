from orator import DatabaseManager, Model
from flask import Flask, render_template, request, url_for

config = {
    'mysql': {
    'driver': 'mysql',
    'host': '172.19.0.2',
    'database': 'db_blog',
    'user': 'root',
    'password': 'root',
    'charset': 'utf8',
    'prefix': ''
    }
}

db = DatabaseManager(config)

Model.set_connection_resolver(db)


class Blog(Model):
    __table__ = 'blog'


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    blog = Blog()
    
    return render_template(
        'index.html',
        blog = blog
        )


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
