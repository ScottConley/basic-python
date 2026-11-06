'''In examples'''

acceptable_inputs = ['apple', 'orange', 'grape']
my_string = 'Hello, World!'

# Use in to check the list

# while True:
    
#     usr_input = input('Enter an allowed fruit: ')
    
#     if usr_input in acceptable_inputs:
#         print('acceptable')
#         break
#     else:
#         print('nope')

# while my_string:
#     usr_input = input('Enter a letter: ')
        
#     if usr_input in my_string:
#         print('That letter is allowed')
#         break
#     else:
#         print('nope')
        
while True:
    usr_input = input('Enter something: ')
    
    if usr_input in ['1', '2', '3', '4']:
        print('that\'s allowed')
        break
    else:
        print('nope')