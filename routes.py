from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from models import Subscriber, TourDate, Album
from sqlalchemy.exc import IntegrityError
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/discography')
def discography():
    albums = Album.query.order_by(Album.release_date.desc()).all()
    return render_template('discography.html', albums=albums)

@app.route('/tour-dates')
def tour_dates():
    dates = TourDate.query.order_by(TourDate.date).all()
    return render_template('tour_dates.html', dates=dates)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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
