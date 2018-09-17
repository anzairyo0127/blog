from flask import Flask, render_template, request, url_for, flash, redirect
from flaskr import app, db
from flaskr.models import Entry


@app.route('/')
def index():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template(
        'index.html',
        entries=entries
    )


@app.route('/post/<post_id>')
def post(post_id):
    entry = Entry.query.filter_by(id=post_id).first_or_404()
    return render_template(
        'post.html',
        entry=entry
    )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/confirm', methods=['POST'])
def confirm():
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
