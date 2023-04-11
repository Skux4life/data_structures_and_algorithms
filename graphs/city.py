class City:
    """Essentially a weighted graph vertex"""

    def __init__(self, name) -> None:
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price


def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_table = {}

    # Using an array as its simpler, priority queue would be more efficient
    unvisited_cities = []

    # Using a hash table to keep track of visited cities
    visited_cities = {}

    # Add the starting cities name as the first key in the cheapest price table with a value of 0
    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city

    # Loop is the core of the algorithm
    # It runs until there are no more unvisited cities
    while current_city:
        # Add current city to visited_cities
        visited_cities[current_city.name] = True
        # Remove current city from unvisited cities
        unvisited_cities.remove(current_city)

        # Iterate over each of the current cities adjacent cities
        for adjacent_city, price in current_city.routes.items():
            # If we discover a new city add it to the list of unvisited cities
            if not visited_cities.get(adjacent_city.name):
                unvisited_cities.append(adjacent_city)
            
            # calculate price from the starting city to the adjacent city using the
            # current city as the 2nd to last stop
            price_through_current_city = cheapest_prices_table[current_city.name] + price

            # if the price from the starting city to the adjacent city is the cheapest we've found so far
            if not cheapest_prices_table[adjacent_city.name] or price_through_current_city < cheapest_prices_table[adjacent_city.name]:
                cheapest_prices_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_table[adjacent_city.name] = current_city.name
        
        # Next city is cheapest unvisited cities
        current_city = min([city for city in cheapest_prices_table if city in unvisited_cities])

    # cheapest prices table is now complete
    shortest_path = []

    # work backwards from final destination
    current_city_name = final_destination.name

    while current_city_name != starting_city.name:
        # Add each current city name we encounter to the shortest path
        shortest_path.append(current_city_name)

        # Use cheapest stopover city table to follow each city to its previous stopover city
        current_city_name = cheapest_previous_stopover_table[current_city_name]

    # Finally add starting city
    shortest_path.append(starting_city.name)

    return shortest_path[::-1]