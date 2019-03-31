from flask import render_template, request
from flask_login import current_user

from models.Entry import Entry
from objects.database import db


def login_page():
    return render_template('login.html')


def login_form_page():
    return render_template('newform.html')


def login_form_review_page():
    return request.form['text']


def login_confirm_exec():
    entry = Entry(
        title=request.form['title'],
        text=request.form['text'],
        name=current_user.id
    )
    db.session.add(entry)
    db.session.commit()
