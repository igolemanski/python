# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

# DO NOT write any print statements.

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

# HINT
# Remember that looping through a Dictionary will only give you the keys and not the values.

# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

# At the end of your program, the print statement will show the final student_scores dictionary.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for student in student_scores:
  scores = student_scores[student]
  if scores > 90:
    student_grades[student] = "Oustanding"
  elif scores > 80:
    student_grades[student] = "Exceeds Expectations"
  elif scores > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)