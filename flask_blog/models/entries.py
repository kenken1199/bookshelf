from flask_blog import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    entries = db.relationship("Entry", backref="users")

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50), unique=True)
    auther = db.Column(db.Text)
    publisher = db.Column(db.Text)

    def __init__(self, users_id=None, title=None, auther=None, publisher=None,):
        self.users_id = users_id
        self.title = title
        self.auther = auther
        self.publisher = publisher