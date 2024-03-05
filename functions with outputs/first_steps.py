# Function with Outputs

# Creating title. This means every first letter of the string will be capitalized. Even if the whole word is capitalized "IVo" or "golEMANsKi" it wil be changed to "Ivo", "Golemanski".

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You haven't entered a name!"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Your first name is {formated_f_name} and your last name is {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))