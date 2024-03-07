# We can create documentation for future references for us or a user so that can help us understand the code in the future. If we hover the mouse on the function "format_name" if will popup a message with the explanation that we wrote.

def format_name(f_name, l_name):
    """Take a first and last name to format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You haven't entered a name!"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Your name is {formated_f_name} and your last name is {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))