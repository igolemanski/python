# https://www.udemy.com/course/100-days-of-code/learn/lecture/19279336#questions

import random
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A peace of code that you can easily you can call over and over again",
    "Random_number": random.random() * 3,
}
# Retrieving items from dictionary
# print(programming_dictionary["Random_number"])

# Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# Create an empty dictionary
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
# programming_dictionary["Bug"] =  "There is a moth in your computer"
# print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    # print(key)
    print(programming_dictionary[key])