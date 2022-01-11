import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)


class Cafe:
    def __init__(
        self,
        name,
        img_url,
        map_url,
        location,
        seats,
        has_toilet,
        has_wifi,
        has_sockets,
        can_take_calls,
        coffee_price,
    ):
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


@app.route("/")  # create a route
def home():  # what's going to happen when make a GET request to the route
    return render_template('index.html')


@app.route("/random")
def get_random_cafe():  # Return a random Cafe when make a GUET request to '/random' route
    with sqlite3.connect("cafes.db") as db_connection:

        db_connection.row_factory = sqlite3.Row

        sql_instruction = """SELECT name, img_url, map_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price FROM cafe ORDER BY RANDOM() LIMIT 1"""

        record = db_connection.execute(sql_instruction).fetchall()

        random_cafe = {}
        for row in record:
            random_cafe.update(dict(row))


        return random_cafe


@app.route("/all")
def get_all_cafe():
    with sqlite3.connect("cafes.db") as db_connection:

        db_connection.row_factory = sqlite3.Row
        db_cursor = db_connection.cursor()

        sql_instruction = """SELECT id, name, img_url, map_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price FROM cafe"""
        db_cursor.execute(sql_instruction)

        all_cafes = {}

        position = 0
        for row in db_cursor.fetchall():
            all_cafes[position] = dict(row)
            position += 1

        return all_cafes


@app.route("/search")
def get_cafe_by_location():
    with sqlite3.connect("cafes.db") as db_connection:

        db_connection.row_factory = sqlite3.Row

        parameter_location = request.args.get(
            "location"
        )  # Variable aims to the argument passed to URL. search?loc=argument
        formatted_parameter = "'" + parameter_location + "'"
        sql_instruction = (
            f"""SELECT * FROM cafe WHERE location={formatted_parameter};""".format(
                formatted_parameter
            )
        )

        db_cursor = db_connection.cursor()
        record = db_cursor.execute(sql_instruction)

        all_cafes = {}
        position = 0
        for row in db_cursor.fetchall():
            all_cafes[position] = dict(row)
            position += 1

        return all_cafes


@app.route("/add", methods=["POST"])  # Default GET method is enabled
def add_new_cafe():
    with sqlite3.connect("cafes.db") as db_connection:

        name = request.form["name"]
        map_url = request.form["map_url"]
        img_url = request.form["img_url"]
        location = request.form["location"]
        seats = request.form["seats"]
        has_toilet = bool(request.form["has_toilet"])
        has_wifi = bool(request.form["has_wifi"])
        has_sockets = bool(request.form["has_sockets"])
        can_take_calls = bool(request.form["can_take_calls"])
        coffee_price = request.form["coffee_price"]

        new_cafe = Cafe(
            name,
            map_url,
            img_url,
            location,
            has_sockets,
            has_toilet,
            has_wifi,
            can_take_calls,
            seats,
            coffee_price,
        )

        db_connection.execute(
            "INSERT INTO cafe (name, img_url, map_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                new_cafe.name,
                new_cafe.img_url,
                new_cafe.map_url,
                new_cafe.location,
                new_cafe.seats,
                new_cafe.has_toilet,
                new_cafe.has_wifi,
                new_cafe.has_sockets,
                new_cafe.can_take_calls,
                new_cafe.coffee_price,
            ),
        )

        response = {"Success": "New cafe added."}
        return response


@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):

    response = {"Success": "Sucessfully update the price."}
    not_found_response = {"Not Found": "A cafe with that id was not found."}

    with sqlite3.connect("cafes.db") as db_connection:

        new_price = request.args.get("new_price")

        sql_query = db_connection.execute(
            "UPDATE cafe SET coffee_price=? WHERE id=?", (new_price, id)
        )

        if sql_query:
            db_connection.commit()
            return response
        else:
            return not_found_response


@app.route("/record_delete/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    with sqlite3.connect("cafes.db") as db_connection:

        api_key = request.args.get("api_key")

        if api_key == "TopSecretAPIKey":
            if db_connection.execute("DELETE FROM cafe WHERE id=?", (cafe_id)):
                db_connection.commit()
                return {"Success": "Sucessfully cafe deleted."}, 200
            else:
                return {
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }, 404
        else:
            return {
                "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
            }, 403


if __name__ == "__main__":
    app.run(debug=True)
