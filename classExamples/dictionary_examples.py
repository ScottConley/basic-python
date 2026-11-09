'''Dictionary Examples'''

# Creating an empty dictionary
empty_dict = {}

# Create a populated dictionary - key:value
stud_ages = {'Roark':24,'Ortiz':22,'Wenc':23}

# Getting a value from a dictionary
print(stud_ages['Wenc'])
print(stud_ages.get('ortiz','Student not found!'))

# Seeing all the values
print(stud_ages.values())

# Looping over the keys of a dictionary
for key in stud_ages:
    print(key)

# Looping over the values
for value in stud_ages.values():
    print(value)   
    
for key in stud_ages:
    # Using the iterating key from each loop. Display value of that key in the dictionary
    # print(stud_ages.get(key))
    print(stud_ages[key])
    
# Looping over the key AND the value
for key,value in stud_ages.items():
    print(f'{key}\'s age is {value}')

# for name,age in stud_ages.items():
#     print(f'{name}\'s age is {age}')
    
# print(stud_ages)