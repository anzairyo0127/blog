from flask import render_template, Markup, redirect, url_for
import markdown

from models.Entry import Entry

FIRST_PAGE_NUM = 1
PER_PAGE = 5


def index_page():
    FIRST_PAGE_NUM = 1
    entries = Entry.query.order_by(Entry.id.desc()).paginate(
        per_page=PER_PAGE,
        page=FIRST_PAGE_NUM,
        error_out=True
    )

    template = render_template(
        'index.html',
        entries=entries
    )
    return template


def thread_page(page_num):
    '''
    show main page
    '''
    page = page_num
    entries = Entry.query.order_by(
        Entry.id.desc()).paginate(
        per_page=PER_PAGE,
        page=page,
        error_out=True
    )
    template = render_template(
        'index.html',
        entries=entries
    )
    return template


def post_page(post_id):
    entry = Entry.query.filter_by(id=post_id).first_or_404()
    texts = Markup(markdown.markdown(entry.text))
    template = render_template(
        'post.html',
        entry=entry,
        texts=texts
    )
    return template


def about_page():
    return render_template('about.html')


def contact_page():
    return render_template('contact.html')


def send_to_mail_page():
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

    return redirect(url_for('blog_route.index'))
