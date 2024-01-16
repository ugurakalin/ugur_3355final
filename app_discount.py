from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
users = {
    "user1": {"id": 1, "name": "Ahmet", "discount": 10},
    "user2": {"id": 2, "name": "Mehmet", "discount": 5},
    "user3": {"id": 3, "name": "Ayşe", "discount": 15},
}

# Dummy hotel data for demonstration
hotels = [
    {"id": 1, "name": "Nex Hotel İstanbul City Center", "rating": 4.5, "comments": 120, "price": 200, "discount": 15},
    {"id": 2, "name": "Casa Nonna Bodrum Otel", "rating": 4.0, "comments": 80, "price": 150, "discount": 20},
    {"id": 3, "name": "Sunda Exclusive By Liberty Fethiye", "rating": 4.8, "comments": 200, "price": 300, "discount": 10},
]

# Function to check if a user is logged in
def is_user_logged_in():
    # In a real-world scenario, you would check the user's session or database for authentication
    return "user_id" in request.cookies

# Function to get the user's discount
def get_user_discount():
    if is_user_logged_in():
        user_id = request.cookies.get("user_id")
        user = users.get(user_id)
        if user:
            return user["discount"]
    return 0

# Function to get the hotel discount
def get_hotel_discount(hotel_id):
    hotel = next((h for h in hotels if h["id"] == hotel_id), None)
    return hotel["discount"] if hotel else 0

@app.route("/")
def index():
    return render_template("index.html", logged_in=is_user_logged_in(), user_discount=get_user_discount(), hotels=hotels)

@app.route("/login")
def login():
    
    response = redirect(url_for("index"))
    response.set_cookie("user_id", "user1")
    return response

if __name__ == "__main__":
    app.run(debug=True)
