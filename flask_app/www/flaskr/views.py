'''
"View" of Flask Web Application  
'''

from flask import Flask, render_template, request, url_for, flash, redirect, Markup
from flaskr import app, db, login_user, current_user, mail, login_required, logout_user, Message
from flaskr.models import Entry
from flaskr.login import User, users, user_loader, request_loader
import markdown

import os


@app.route('/')
def index():
    '''
    show main page
    '''
    page = 1
    entries = Entry.query.order_by(Entry.id.desc()).paginate(
        per_page=5, page=page, error_out=True)
    return render_template(
        'index.html',
        entries=entries
    )


@app.route('/thread/<int:page_num>')
def thread(page_num):
    '''
    show main page
    '''
    page = page_num
    entries = Entry.query.order_by(Entry.id.desc()).paginate(
        per_page=5, page=page, error_out=True)
    return render_template(
        'index.html',
        entries=entries
    )


@app.route('/post/<post_id>')
def post(post_id):
    entry = Entry.query.filter_by(id=post_id).first_or_404()
    texts = Markup(markdown.markdown(entry.text))
    return render_template(
        'post.html',
        entry=entry,
        texts=texts
    )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/send_to_mail', methods=['POST'])
def send_to_mail():
    name = request.form['name']
    mes = request.form['message']
    if name == '' or mes == '':
        return 'No message or No name is not send'
    else:
        msg = Message(
            subject='お名前:{name}さんからのメッセージ'.format(name=name),
            body=mes,
            sender=os.getenv('MAIL_USERNAME'),
            recipients=[os.getenv('MAIL_USERNAME')]
        )
        mail.send(msg)

    return redirect(url_for('index'))


@app.route('/form')
@login_required
def form():
    if not current_user.id:
        return redirect(url_for('login'))
    else:
        return render_template('form.html')


@app.route('/form_review', methods=['POST'])
@login_required
def form_review():
    if not current_user.id:
        return redirect(url_for('login'))
    else:
        title = request.form['title']

        return title


@app.route('/confirm', methods=['POST'])
@login_required
def confirm():
    entry = Entry(
        title=request.form['title'],
        text=request.form['text'],
        name=current_user.id
    )
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('form'))

    return 'Bad login'


@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/list_of_article')
def list_of_article():
    logout_user()
    page = 1
    entries = Entry.query.order_by(Entry.id.desc()).paginate(
        per_page=5, page=page, error_out=True)
    return render_template(
        'index.html',
        entries=entries
    )
    return render_template('admin_art_list.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
