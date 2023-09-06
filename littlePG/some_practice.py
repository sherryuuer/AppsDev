# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# name = "chaonanwang"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)

# names = ["beth", "wang", "zhang", "angela", "Elanor"]
# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)


# # print the number in both file
# with open("file1.txt") as f:
#     list1 = [n for n in f.readlines()]
# with open("file2.txt") as f:
#     list2 = [n for n in f.readlines()] 
# result = [int(n) for n in list1 if n in list2]
# print(result)


# list/dictionary one line code.
import random
names = ["beth", "wang", "zhang", "angela", "Elanor"]
students_scores = {student:random.randint(30,100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
