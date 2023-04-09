class City:
    """Essentially a weighted graph vertex"""

    def __init__(self, name) -> None:
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price