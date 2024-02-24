country = input("Input a country you have visited: ") # Add country name
visits = int(input("How many times you have visited?: ")) # Number of visits
list_of_cities = eval(input()) # create list from 

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 4,
        "cities": ["Berlin", "Hambur", "Stuttgart"]
    },
]

# TODO: Write the function that will allow you new countries to be added to travel_log
def add_new_country(country, visits, list_of_cities):
    position = travel_log[2]["country"]        

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} {travel_log[2]['cities']}")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")