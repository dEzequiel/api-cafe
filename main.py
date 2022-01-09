from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import sqlite3

app = Flask(__name__)

##Connect to Database
db_connection = sqlite3.connect("cafes.db")
db_cursor = db_connection.cursor()



# ##Cafe TABLE Configuration
# class Cafe(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), unique=True, nullable=False)
#     map_url = db.Column(db.String(500), nullable=False)
#     img_url = db.Column(db.String(500), nullable=False)
#     location = db.Column(db.String(250), nullable=False)
#     seats = db.Column(db.String(250), nullable=False)
#     has_toilet = db.Column(db.Boolean, nullable=False)
#     has_wifi = db.Column(db.Boolean, nullable=False)
#     has_sockets = db.Column(db.Boolean, nullable=False)
#     can_take_calls = db.Column(db.Boolean, nullable=False)
#     coffee_price = db.Column(db.String(250), nullable=True)

#     def to_dict(self):
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#     def __init__(self, name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price):
#         self.name = name
#         self.map_url = map_url
#         self.img_url = img_url
#         self.location = location
#         self.has_sockets = has_sockets
#         self.has_toilet = has_toilet
#         self.has_wifi = has_wifi
#         self.can_take_calls = can_take_calls
#         self.seats = seats
#         self.coffee_price = coffee_price


# @app.route("/") # create a route
# def home(): # what's going to happen when make a GET request to the route
#     return render_template("index.html")


# @app.route("/random")    
# def get_random_cafe():  # Return a random Cafe when make a GUET request to '/random' route
#     cafes = db.session.query(Cafe).all() # List of objects made by query. 'Query.one() in case of want only one object'
#     random_cafe = random.choice(cafes)  # Instance of the sub-object selected    

#     return jsonify(cafe={
#         "id": random_cafe.id,
#         "name": random_cafe.name,
#         "location": random_cafe.location,
#         "has_wifi": random_cafe.has_wifi,
#         "can_take_calls": random_cafe.can_take_calls,
#         "coffee_price": random_cafe.coffee_price,
#     })

# @app.route("/all")
# def get_all_cafe():

#     cafes_list = []
#     cafes = db.session.query(Cafe).all() # All objects in a list
    
#     for cafe in cafes:
#         cafes_dict = {"id": cafe.id, "name": cafe.name, "location": cafe.location, "has_wifi": cafe.has_wifi, "can_take_call": cafe.can_take_calls, "coffe_price": cafe.coffee_price}
#         cafes_list.append(cafes_dict)

#     return jsonify(cafes=cafes_list)

# @app.route("/search")
# def get_cafe_by_location():

#     query_location = request.args.get("loc") # Variable aims to the argument passed to URL. search?loc=argument
#     cafes = db.session.query(Cafe).filter_by(location=query_location) 
#     cafes_list = []

#     if cafes:
#          for cafe in cafes:
#             cafes_dict = {"id": cafe.id, "name": cafe.name, "location": cafe.location, "has_wifi": cafe.has_wifi, "can_take_call": cafe.can_take_calls, "coffe_price": cafe.coffee_price}
#             cafes_list.append(cafes_dict)
#     else:
#         return jsonify(error={"Not Found": "Sorry, we dont' have a cafe at that location."})
    
#     return jsonify(cafe=cafes_list)

# @app.route("/add", methods=['POST']) #Default GET method is enabled
# def add_new_cafe():
#     name=request.form.get("name")
#     map_url=request.form.get("map_url")
#     img_url=request.form.get("img_url")
#     location=request.form.get("loc")
#     has_sockets=bool(request.form.get("sockets"))
#     has_toilet=bool(request.form.get("toilet"))
#     has_wifi=bool(request.form.get("wifi"))
#     can_take_calls=bool(request.form.get("calls"))
#     seats=request.form.get("seats")
#     coffee_price=request.form.get("coffee_price")

#     new_cafe = Cafe(name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price)

#     db.session.add(new_cafe)
#     db.session.commit() # .commit() is used when wants the information stays in database, we writing to the database and wants the information to persists
#     return jsonify(response={"Success": "New cafe added."})

# ## HTTP GET - Read Record

# ## HTTP POST - Create Record

# ## HTTP PUT/PATCH - Update Record

# ## HTTP DELETE - Delete Record


# if __name__ == '__main__':
#     app.run(debug=True)
