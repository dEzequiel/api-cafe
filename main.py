from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

from sqlalchemy.sql import selectable

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/") # create a route
def home(): # what's going to happen when make a GET request to the route
    return render_template("index.html")


@app.route("/random")    
def get_random_cafe():  # Return a random Cafe when make a GUET request to '/random' route
    cafes = db.session.query(Cafe).all() # List of objects made by query. 'Query.one() in case of want only one object'
    random_cafe = random.choice(cafes)  # Instance of the sub-object selected    

    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "location": random_cafe.location,
        "has_wifi": random_cafe.has_wifi,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

@app.route("/all")
def get_all_cafe():

    cafes_list = []
    cafes = db.session.query(Cafe).all() # All objects in a list
    
    for cafe in cafes:
        cafes_dict = {"id": cafe.id, "name": cafe.name, "location": cafe.location, "has_wifi": cafe.has_wifi, "can_take_call": cafe.can_take_calls, "coffe_price": cafe.coffee_price}
        cafes_list.append(cafes_dict)

    return jsonify(cafes=cafes_list)

@app.route("/search")
def get_cafe_by_location():

    query_location = request.args.get("loc") # Variable aims to the argument passed to URL
    cafes = db.session.query(Cafe).filter_by(location=query_location) 
    cafes_list = []

    if cafes:
         for cafe in cafes:
            cafes_dict = {"id": cafe.id, "name": cafe.name, "location": cafe.location, "has_wifi": cafe.has_wifi, "can_take_call": cafe.can_take_calls, "coffe_price": cafe.coffee_price}
            cafes_list.append(cafes_dict)
    else:
        return jsonify(error={"Not Found": "Sorry, we dont' have a cafe at that location."})
    
    return jsonify(cafe=cafes_list)

@app.route("/add", methods=['POST']) #Default GET method is enabled
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        location=request.form.get("loc"),
        has_wifi=request.form.get("wifi"),
        can_take_calls=request.form.get("calls"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit() # .commit() is used when wants the information stays in database, we writing to the database and wants the information to persists

    return jsonify(response={"Success": "New cafe added."})

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
