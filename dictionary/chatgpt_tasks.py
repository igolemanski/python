# 1. Create a dictionary representing information about a person, including their name, age, and occupation.
# person = {
#     "name": "Niki",
#     "tall": 180,
#     "weight": 84,
#     "age": 44,
# }

# 2. Access and print individual values from the dictionary created in Task 1.
# name_of_person = person["name"]
# print(name_of_person)

# 3. Update the age of the person in the dictionary from Task 1.
# person["age"] = 33
# print(person)

# 4. Add a new key-value pair to the dictionary, representing the person's city of residence.
# person["city"] = "Plovdiv"
# print(person)

# 5. Remove the occupation key-value pair from the dictionary.
# del person["tall"]
# print(person)

# 6. Iterate through the dictionary and print each key-value pair.
# for rotate in person:
#     print(person[rotate])

# 7. Check if a specific key (e.g., "occupation") exists in the dictionary.
# isTrue = False
# occupation = input()
# if occupation in person:
#     isTrue = True
#     print(f"{occupation} is in the dictionary")
# else:
#     print(f"{occupation} is not in the dictionary")


# 8. Determine the number of key-value pairs in the dictionary.
# print(len(person))


# 9. Create a nested dictionary representing information about multiple people, each with their own name, age, and occupation.
dictionary = {
    "person3": {"name": "Gosho", "age": 42, "occupation": "Plovdiv"},
    "person1": {"name": "Ivo", "age": 38, "occupation": "Plovdiv"},
    "person2": {"name": "Niki", "age": 30, "occupation": "Plovdiv"},

}

# 10. Create a new dictionary using dictionary comprehension that includes only people who are above a certain age. Here we are involved with task 9
age_restriction = 35
filtering_dictionary = {}
for key, value in dictionary.items():
    if value["age"] > age_restriction:
        filtering_dictionary[key] = value
    

# 11. Sort the dictionary from Task 9 based on the age of each person.
sorted(filtering_dictionary.items())

# 12. Merge two dictionaries into a new dictionary.
merged_dictionaries = {**dictionary, **filtering_dictionary}

# 13. Modify the nested dictionary from Task 9 to store multiple cities for each person.

# 14. Dictionary Methods: explore and use dictionary methods such as keys(), values(), and items().

# 15. Check if a specific value (e.g., "Engineer") exists in the dictionary.


