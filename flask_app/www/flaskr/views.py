from flask import Flask, render_template, request, url_for, flash
from flaskr import app, db
from flaskr.models import Entry


@app.route('/', methods=['GET', 'POST'])
def index():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template(
        'index.html',
        entries=entries
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
