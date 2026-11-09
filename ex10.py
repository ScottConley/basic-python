'''Exercise 10'''

# Dictionary of student grades
grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

print(grades)
# 1. Add a new student named "Emma" with a grade of 90.

grades["Emma"] = 90
print(grades)

# 2. Update Bob's grade to 82.

grades.update({"Bob": 82})
print(grades)

# 3. Calculate and print the average grade of all students.
grades_list = []
for key in grades:
    grades_list.append(grades[key])
    
avg = sum(grades_list)/len(grades_list)
print(f'The class average is: {avg}')

# 4. Find and print the student with the highest grade.

# <---- The below is to demonstrate how lambda functions work!! ----->

def get_score(person):
    return person[1]

sort_grade = dict(sorted(grades.items(), key=get_score, reverse = True))
print(f'function sort: {sort_grade}')

# <---- The above is to demonstrate how lambda functions work!! ----->

sorted_grade = dict(sorted(grades.items(), key=lambda item: item[1], reverse = True))
print(f'lambda sort: {sorted_grade}')

first_pair = list(sorted_grade.items())[0]
print(first_pair)

# <---- Here's a way to just return the maximum pair ---->

max_val = max(grades.items(), key=lambda item: item[1])
print(f'Here\'s just the max pair: {max_val}')

print(f'{max(grades, key = grades.get)} has the top score of {max(grades.values())}!')

# 5. Print all students and their grades in a readable format.

for key in grades:
    print(f'{key} has a grade of {grades[key]}')