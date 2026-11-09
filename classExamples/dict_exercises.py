'''Dict Exercises'''

# Dictionary of student grades
grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

# 1. Add a new student named "Emma" with a grade of 90.
grades['Emma'] = 90

# 2. Update Bob's grade to 82.
grades['Bob'] = 82
grades.update({'Bob':82})

# 3. Calculate and print the average grade of all students.
total = 0
for grade in grades.values():
    total += grade
avg = total / len(grades)
print(f'The average student grade is {avg}')

# print(sum(grades.values()) / len(grades)

# 4. Find and print the student with the highest grade.
# Creating a variable to track the highest grade
highest_grade = 0

for student, grade in grades.items():
    # Comparing each grade in dict to highest_grade
    if grade > highest_grade:
        highest_grade = grade
        highest_student = student

# Utilizing max to target only the values
highest_grade2 = max(grades.values())

for student in grades:
    # Finding which student had the highest grade
    if grades[student] == highest_grade2:
        highest_student2 = student
        
print(highest_grade, highest_grade2)
print(highest_student, highest_student2)

# Utilizing max and key - this is more advanced
highest_student_all_in_one = max(grades, key=grades.get)
print(f'Output of the all in one. {highest_student_all_in_one} has the highest grade. With a score of {grades[highest_student_all_in_one]}')

# 5. Print all students and their grades in a readable format.
for student, grade in grades.items():
    print(f'{student}\'s grade is {grade}')
    