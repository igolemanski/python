# READING FILES. Reading from external files, like txt, csv, html etc. We are using python read command. We use "open" and then specify the path to the file or if it is in the same directory we just type the name of the file. After that we give the priviliges. For example "r" for read, "w" for write, "a" for append, "r+" for reading and writing.
employee_file = open("readingfile.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


# WRITING AND APPENDING TO FILES. With \n character we are adding new line to the file. If we use "w" we overwrite the whole file and everything else will be removed. We can use "w" priviliges to create a new file.
employee_file = open("readingfile.txt", "a")
employee_file.write("\nIco - Suzuki GSXR750")
employee_file.close()

employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML file</p>")
employee_file.close()