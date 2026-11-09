'''Dictionary Examples'''

empty_dict = {}

student_ages = {
    # key : value
    "Conley" : 35,
    "Roark" : 24,
    "Ortiz" : 22,
    "Wenc" : 23
}

print(student_ages)
print(student_ages["Conley"])
print(student_ages.get("Roark"))
print(student_ages.get("roark", "Student not found."))

# See all values

print(student_ages.values())

age_list = student_ages.values()
print(age_list)

# Looping over dicts

for key in student_ages:
    print(f"{key}: {student_ages[key]}")
    
# Looping over values

for value in student_ages.values():
    print(value)
    
for key in student_ages:
    print(student_ages.get(key))
    print(student_ages[key],"\n")
    
# Looping over key and value

for key, value in student_ages.items():
    print(f"{key}: {value}")
    
# Nested dictionary

nested_dict = {
    0 : {
        'name' : 'Stewart',
        'hobbies' : ['Hurting people', 'Stealing', 'Test Compromise'],
        'follow-on' : 'SEM'
        },
    1 : {
        'name' : 'Conley',
        'hobbies' : ['Helping people', 'Donating', 'Test Compromise'],
        'follow-on' : 'ADA'
    }
}

print(nested_dict)
print(nested_dict[0])
print(nested_dict[0]['hobbies'])
print(nested_dict[0]['hobbies'][2])
print(nested_dict[0]['hobbies'][2][5])

for user, details in nested_dict.items():
    print(f'ID: {user}')
    for key, value in details.items():
        print(f'{key}: {value}')
