from datetime import datetime

from objects.database import db


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
