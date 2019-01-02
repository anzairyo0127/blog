'''
Models
'''


from datetime import datetime

from flaskr import db


class Entry(db.Model):
    '''
    MRD
    '''
    __tablename__ = 'entry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
            id=self.id, title=self.title)


class Users(db.Model):
    '''
    MRD
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    emails = db.Column(db.Text)
    passwords = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<Entry email={email} password={password}>'.format(
            email=self.emails, password=self.passwords)
