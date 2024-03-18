# METHODS

# upper() method. Makes all characters in a string uppercase.
# phrase = "Academy Course"
# print(phrase.upper())

# isupper() method together with upper(). Returns true if all of the characters in a string are uppercase, and false if they aren't. Both are useful for formatting data that is dependant on case.
# phrase = "Academy Course"
# print(phrase.upper().isupper())

# Prints the total number of characters in a string.
# print(len(phrase))

# Accessing string character
# print(phrase[8])

# Finding the index of a string
# print(phrase.index("o"))

# Replacing strings
# b = "K"
# print(phrase.replace("a", "b"))

# find() method. In the example it is seaching in 'alphabet' varibale for the 4 object located in 'text' variable.
# text = 'Hello World'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# position = alphabet.find(text[4])
# print(position)


# List index() Method
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)


# items() Method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# car["year"] = 2018
# print(x)


# remove() Method removes an element with specified calue
fruits = ['apple', 'banana', 'cherry']
x = fruits.remove("cherry")
print(fruits)