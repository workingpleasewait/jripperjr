from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from models import Subscriber, GigDate, BandMember, BlogPost
from sqlalchemy.exc import IntegrityError
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biography')
def biography():
    band_members = BandMember.query.all()
    return render_template('biography.html', band_members=band_members)

@app.route('/discography')
def discography():
    return render_template('discography.html')

@app.route('/gigs')
def gigs():
    dates = GigDate.query.order_by(GigDate.date).all()
    return render_template('tour_dates.html', dates=dates)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        # Here you would typically save this information to the database
        # For now, we'll just return a success message
        return jsonify({"success": True, "message": "Thank you for your message. We will get back to you soon!"})
    return render_template('contact.html')

@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        new_subscriber = Subscriber(email=email)
        try:
            db.session.add(new_subscriber)
            db.session.commit()
            return jsonify({"success": True, "message": "Successfully subscribed!"})
        except IntegrityError:
            db.session.rollback()
            return jsonify({"success": False, "message": "Email already subscribed."})
    return jsonify({"success": False, "message": "Invalid email address."})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
