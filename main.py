



# "floor" function will get the lower number and will chopoff the decimal point.
# To get access to some specific functions, they need to be imported with the sentence "from math import *". Some of the functions are "floor", "ceil" etc.
# from math import *
# print(floor(6.7))
# "ceil" function will get the higher number and will chopoff the decimal point.
# print(ceil(1.6))
# square root of a number we get with the function "sqrt"
# print(sqrt(36))


# GETTING INPUT
# name = input("What is your name: ")
# age = input("How old are you: ")
# print("Hello, " + name + "!" " You are " + age + "!")


# CALCULATOR GAME
# num1 = input("Enter number 1: ")
# num2 = input("Enter number 2: ")
# result = float(num1) + float(num2)
# print(result)


# Mad libs GAME
# car = input("Enter you car brand: ")
# model = input("Enter the model of your car: ")
# engine = input("Enter the engine size: ")
# color = input("What is the color of your car: ")
# motorcycle = input("What is your motorcycle: ")
# motorcycle_model = input("What model it is: ")
# motorcycle_engine = input("The engine size is: ")
# print("My car is " + car + " " + model + "." " Engine size is " + engine + " and it is " + color + " color.")
# color = input("Enter you color: ")
# print("I also own a motorcycle " + motorcycle + " " + motorcycle_model + " and the engine size is " + motorcycle_engine + "." + " It's color is " + color + ".")


# LISTS. How lists work. In lists we use parenthesis []. We can change the value in lists. For example friends[1] = "Madonna"
# friends = ["Gosho", "Jivko", "Ico", "Nasko", "Svetlio"]
# print(friends[1])
# print(friends[0:2])
# friends[2] = "Koko"
# print(friends[2])


# LIST Functions
# lucky_num = [4, 8, 101, 16, 23, 42]
# friends = ["Gosho", "Jivko", "Ico", "Nasko", "Svetlio", "Pesho", "Pesho"]
# Extend function
# friends.extend(lucky_num)
# Append function
# friends.append("JOJO")
# Insert function
# friends.insert(2, "Simo")
# Remove function
# friends.remove("Nasko")
# Clear function. This will remove all elements from the array(list)
# friends.clear()
# To remove the last element from the array. Or we can specify the element in the parenthesis
# friends.pop()
# To check if an element is in the array
# print(friends.index("Pesho"))
# To check how many elements are repeating in the array(list)
# print(friends.count("Gosho"))
# To sort a list in alphabetical order
# Copy function
# friends2 = friends.copy()
# print(friends2)
# print(friends)


# TUPLES -storing data structure. The values can not be changed because in tuples we use parenthesis (). If we try to change it with coordinates[1] = 10, we will get an error.
# coordinates = (3, 5)
# print(coordinates[1])


# FUNCTIONS. To create a function we use "def". To run trough the function we need to call it, by using the last line on say_hi()
# def say_hi(name, age):
#     print("Hello " + name + "." " You are " + age + " old.")
#
# say_hi("Ivo", "37")
# say_hi("Nikol", "30")

# Exercise
# def vehicles(brand, model, year):
#     print("What car you've had: " + brand + " " + model + ". " + "Year: " + str(year))
#
# vehicles("Opel", "Astra", 1998)
# vehicles("Hyundai", "i40", 2014)


# RETURN STATEMENT. return will give us information back from a function(Like a value or a statement). After the return statement we are not allowed to add any other code. Basically it breaks us out of the function.
# def cube(num):
#     return num*num*num
# result = cube(4)
# print(result)


# IF STATEMENT. It is based on conditions.
# is_male = False
# is_tall = True
#
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male and you are tall")
# else:
#     print("You are not male and not tall or both")


# IF STATEMENT AND COMPARISON. Here we use comparison operators.
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(30, 14, 55))


# CALCULATOR
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator: ")
# num2 = float(input("Enter a second number: "))
#
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# else:
#     print("invalid operator")

# ELEVATOR Game
# elevator = float(input("Enter your floor: "))
# if elevator >= 1 and elevator <= 4:
#     print("You are going to floor 1")
# elif elevator == 2:
#     print("You are going to floor 2")
# elif elevator == 3:
#     print("You are going to floor 3")
# elif elevator == 4:
#     print("Private floor, you need a key card")
# else:
#     print("incorrect floor")


# DICTIONARIES. Allows to store information: key_value_pairs. Dictionaries are working with the curly brackets only {}. We can sign different type of "keys" like in the example below.
# monthConversions = {
#     1: "January",
#     2: "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(monthConversions.get("ggg", "Not a valid key"))
# print(monthConversions[1])
# print(monthConversions["Oct"])


# WHILE LOOP. Loop trough and execute a block of code multiple times until a certain conditions is True.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done with loop")


# BUILDING A GUESSING GAME
# secret_word = "car"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("You lost. OUT OF GUESSES")
# else:
#     print("You guessed the word is: " + guess)


# temperature = 8
# guess_temperature = ""
# count = 0
# count_limit = 3
# out_of_guesses = False
# while guess_temperature != temperature and not(out_of_guesses):
#     if count < count_limit:
#         guess_temperature = int(input("What is the temperature now: "))
#         count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of guesses")
# else:
#     print("You guessed it.")


# FOR LOOP. After "for" we basically create variable that will loop trough every symbol(letter or number or anything) in the quotation marks and it will print it in different row.
# for letter in "Pythong cours"
#     print(letter)

# friends = ["Nikol", "Jivko", "Gosho"]
# for index in friends:
#     print(index)

# for index in range(2, 5):
#     print(index)

# friends = ["Nikol", "Jivko", "Gosho"]
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("not first iteration")


# EXPONENT FUNCTION. Allowing us to take a certain number and raise it to specific power.
# print(2**3)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result *= base_num
#     return result
# print(raise_to_power(2, 3))


# # 2D lists & Nested loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(number_grid[2][1])


# # number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for row in number_grid:
#     for col in row:
#         print(col)




# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# highest_num = student_scores[0]
# for i in student_scores:
#   if i > highest_num:
#     highest_num = i
# print(f"The highest score in the class is: {highest_num}")