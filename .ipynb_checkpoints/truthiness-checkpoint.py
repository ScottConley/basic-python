'''Testing Truthiness'''

txt_upper = 'Hello, World!'
txt_lower = 'hello, world.'

print(txt_upper.islower())
print(txt_lower.islower())

usr_input = input('Enter something: ') or 'defualt'

print(f'User input is lowercase? {usr_input.islower()}')

if usr_input.islower():
    print(f'{usr_input} is lowercase!')
    
my_string = ''
    
if my_string:
    print('It\'s true! Non empty strings are true!')
else:
    print('It\'s false! Empty strings are false!')
    
my_num = 0

if my_num:
    print("It's true!")
else:
    print("It's false!")