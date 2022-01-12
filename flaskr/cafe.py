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