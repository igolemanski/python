# How functions are working:

# def greet(name):
#     print(f"Hello {name}")
# greet("Ivo")


# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}")
# greet_with(name = "Ivo", location = "Plovdiv")


import math
def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / cover) 
    print(f"You'll need {round(num_of_cans)} cans of paint.")

# Define a function called paint_calc() so the code below works.   

test_h = int(input("Enter wall height: ")) # Height of wall (m)
test_w = int(input("Enter wall width: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

