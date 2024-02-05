# We are using random module to create random numbers which we specify in the parentheses
import random

# Creates random number between 1 and 10, including them
random_integer = random.randint(1, 10)
print(random_integer)

# It prints number between 0 and 1, but does not include 1
random_float = random.random()
print(random_float)

# To get different random floating number we can multiply the random number by any other number
random_float_expand = random.random() * 10
print(random_float_expand)