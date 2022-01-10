import random
import sqlite3
import json

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Cafe():
    def __init__(self, name, img_url, map_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price
    
# prueba = Cafe('prueba', 'prueba', 'prueba', 'prueba', 2, True, True, True, True, '2')
# x = f'''INSERT INTO cafe (name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price) VALUES (
#         '{prueba.name}', '{prueba.map_url}', '{prueba.img_url}', '{prueba.location}', '{prueba.seats}', '{prueba.has_toilet}', '{prueba.has_wifi}', '{prueba.has_sockets}', '{prueba.can_take_calls}', '{prueba.coffee_price}'
# )'''

# db_cursor.execute(x)
# db_connection.commit()


@app.route("/") # create a route
def home(): # what's going to happen when make a GET request to the route
    return render_template("index.html")


@app.route("/random")    
def get_random_cafe():  # Return a random Cafe when make a GUET request to '/random' route
    with sqlite3.connect("cafes.db") as db_connection:

        db_connection.row_factory = sqlite3.Row

        sql_instruction = '''SELECT name, img_url, map_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price FROM cafe ORDER BY RANDOM() LIMIT 1'''

        record = db_connection.execute(sql_instruction).fetchall()
        
        random_cafe = {}
        for row in record:
            random_cafe.update(dict(row))

        db_connection.close()

        return random_cafe

@app.route("/all")
def get_all_cafe():
    with sqlite3.connect("cafes.db") as db_connection:

        db_connection.row_factory = sqlite3.Row
        db_cursor = db_connection.cursor()

        sql_instruction = '''SELECT * FROM cafe'''
        db_cursor.execute(sql_instruction)

        all_cafes = {}

        position = 0
        for row in db_cursor.fetchall():
            all_cafes[position] = dict(row)
            position += 1

        return all_cafes
    
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


if __name__ == '__main__':
    app.run(debug=True)
