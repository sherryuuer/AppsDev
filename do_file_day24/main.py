# file = open("do_file_day24/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("do_file_day24/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("do_file_day24/my_file.txt", mode="w") as file:
    file.write("New text.")

with open("do_file_day24/my_file.txt", mode="a") as file:
    file.write("\nAnother new text.") # \n will help you add a new line.

with open("do_file_day24/new_file.txt", mode="w") as file:
    file.write("a new file is created.")
