from app import db
from datetime import datetime

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

class GigDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)

class BandMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('band_member.id'), nullable=False)
    author = db.relationship('BandMember', backref=db.backref('blog_posts', lazy=True))
