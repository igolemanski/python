country = input("Input a country you have visited: ") # Add country name
visits = int(input("How many times you have visited?: ")) # Number of visits
list_of_cities = input("Enter cities you have been: ") # create list from 

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# TODO: Write the function that will allow you new countries to be added to travel_log
def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} {travel_log[2]['cities']}")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")