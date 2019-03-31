'''
"View" of Flask Web Application  
'''
import os

from flask import Flask, render_template, request, url_for, flash, redirect, Markup, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
import markdown

from views import blog_view, error_view, login_view
from helper.login import User, users


blog_route = Blueprint('blog_route', __name__)


@blog_route.route('/')
def index():
    return blog_view.index_page()


@blog_route.route('/thread/<int:page_num>')
def thread(page_num):
    return blog_view.thread_page(page_num)


@blog_route.route('/post/<post_id>')
def post(post_id):
    return blog_view.post_page(post_id)


@blog_route.route('/about')
def about():
    return blog_view.about_page()


@blog_route.route('/contact')
def contact():
    return blog_view.contact_page()


@blog_route.route('/send_to_mail', methods=['POST'])
def send_to_mail():
    return blog_view.send_to_mail_page()


@blog_route.route('/form')
@login_required
def form():
    if not current_user.id:
        return redirect(url_for('blog_route.login'))
    else:
        return login_view.login_form_page()


@blog_route.route('/form_review', methods=['POST'])
@login_required
def form_review():
    if not current_user.id:
        return redirect(url_for('blog_route.login'))
    else:
        return login_view.login_form_review_page()


@blog_route.route('/confirm', methods=['POST'])
@login_required
def confirm():
    login_view.login_confirm_exec()
    return redirect(url_for('blog_route.index'))


@blog_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return login_view.login_page()

    elif request.method == 'POST':
        if request.form['password'] == users[request.form['email']]['password']:
            user = User()
            user.id = request.form['email']
            login_user(user)
            return redirect(url_for('blog_route.form'))
        else:
            return 'Bad login'
    else:
        return 'Bad login'


@blog_route.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id


@blog_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog_route.index'))


@blog_route.errorhandler(404)
def page_not_found(e):
    return error_view.page_not_found_page()
