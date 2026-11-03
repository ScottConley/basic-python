'''Split and join examples'''

# Splitting a user input

first_name, last_name = input('Enter your first and last name: ').split()[::2]

print(first_name)
print(last_name)

# Unpacking a list

num1, num2 = [9, 10]

print(f'{num1}, {num2}')
print(f'{num1+num2}')

# Splitting on something not a space

my_string = 'joe-schmoe'
joe_name = my_string.split('-')
joe_first, joe_last = my_string.split('-')

print(joe_name)
print(f'{joe_first} {joe_last}')

# Joining a list into a string

' '.join(joe_name)
print(joe_name)