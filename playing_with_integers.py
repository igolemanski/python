# TASK 1
num_char = len(input("What is your name "))
new_num_char = str(num_char)
print("Hello your name has " + new_num_char + " characters")

# TASK 2
two_digit_number = input("Enter a two digit number ")

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

calc = num1 + num2
print(calc)

# TASK 3
height = input()
weight = input()
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# TASK 4
age = input()
max_age = 90
one_year_weeks = 52
x = (max_age - int(age)) * one_year_weeks
print(f"You have {x} weeks left.")