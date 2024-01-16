from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Float)
    comments_count = db.Column(db.Integer)
    price = db.Column(db.Float)
    special_discount = db.Column(db.Float)
    amenities = db.Column(db.String(500))
    coordinates = db.Column(db.String(20))

# Assume you have created the necessary tables and added some sample data to the 'users' and 'hotels' tables

@app.route('/')
def home():
    user_name = session.get('user_name', 'Guest')

    # Determine the upcoming weekend
    today = datetime.now().date()
    friday = today + timedelta(days=(4 - today.weekday() + 7) % 7)
    sunday = friday + timedelta(days=2)

    # Fetch hotels available for the coming weekend, ordered by points DESCENDING in the COUNTRY
    hotels = (
        Hotel.query.filter(Hotel.check_in_date.between(friday, sunday))
        .order_by(Hotel.rating.desc(), Hotel.city)
        .limit(3)
        .all()
    )

    return render_template('home.html', user_name=user_name, hotels=hotels)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check login credentials (replace with actual authentication logic)
        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_name'] = user.email.split('@')[0]
            return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('home'))

@app.route('/search_results')
def search_results():
    # Implement logic to fetch search results from the database based on user input
    # You might get search parameters from the request object
    return render_template('search_results.html')

@app.route('/hotel_detail/<int:hotel_id>')
def hotel_detail(hotel_id):
    # Fetch details of a specific hotel based on the provided hotel_id
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template('hotel_detail.html', hotel=hotel)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
