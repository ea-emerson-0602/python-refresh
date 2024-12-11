students = {}
students_sheet = 0


def students_grades(name, grade):
    students[name] = grade

# test
# 2nd commit test
while True:

    student_name = str(input(f"Write a student's name (or type 'done' to exit): ")).capitalize()
    print(students.keys())
    if student_name == "Done":
        break
    elif student_name == "":
        print("Please type in a name!")
        continue
    elif student_name in students.keys():
        print(f"Student with the name: {student_name} already exists!")
        update_grade = input(f"Do you want to update the grade for {student_name}? (Type 'yes' or 'no' only). ")
        update_grade.lower()
        if update_grade == "yes":
            update_grade = int(input(f"Type in the new grade for {student_name}: "))
            print(f"Grade updated for {student_name} successfully.")
        elif update_grade == "no":
            continue
        else:
            print("Only 'yes' or 'no' is allowed!")
        student_grade=update_grade

    else:
        student_grade = input(f"Write the grade for {student_name}: ")
        while student_grade == "":
            print("Please type in a grade number!")
            student_grade = input(f"Type in the correct grade for {student_name}: ")
    # student_grades=int(student_grade)
    students_grades(student_name, student_grade)

raw_grades_list = list(students.values())
grades_list = []
for grade in raw_grades_list:
    new_grade = int(grade)

    grades_list.append(new_grade)


def average(average_grade):
    average_grade = round(sum(grades_list) / len(students), 2)
    above_average = 0
    for individual_grade in grades_list:
        if individual_grade > average_grade:
            above_average += 1
    print(above_average)

    print(
        f"The average grade of the {len(students)} students is: {average_grade}, and {above_average} student{"" if above_average <= 1 else "s"} scored above average. ")


average(students.values())
# #
highest = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
students_list = list(highest.items())


def find_top_students(students_lists):
    max_score = max(student[-1] for student in students_lists)
    return {
        'names': [student[0] for student in students_lists if student[-1] == max_score],
        'score': max_score
    }


def find_lowest_students(students_lists):
    min_score = min(student[-1] for student in students_lists)
    return {
        'names': [student[0] for student in students_lists if student[-1] == min_score],
        'score': min_score
    }


highest_students = find_top_students(students_list)
best_student = highest_students['names']
#
if len(best_student) <= 1:
    best_student_as_string = ", ".join(best_student)
else:
    best_student_as_string = ", ".join(best_student[:-1]) + f", and {best_student[-1]}"
print(
    f"""The best student{"" if len(best_student) <= 1 else "s"} {"was" if len(best_student) <= 1 else "were"} {best_student_as_string}, and the highest grade scored was {highest_students['score']}""")

# Assuming students_list is defined earlier in your code
lowest_students = find_lowest_students(students_list)
worst_student = lowest_students['names']

if len(worst_student) <= 1:
    worst_student_as_string = ", ".join(worst_student)
else:
    worst_student_as_string = ", ".join(worst_student[:-1]) + f" and {worst_student[-1]}"
print(
    f"""The worst student{"" if len(worst_student) <= 1 else "s"} {"was" if len(worst_student) <= 1 else "were"} {worst_student_as_string}, and the lowest grade scored was {lowest_students['score']}""")
#
print(students)
