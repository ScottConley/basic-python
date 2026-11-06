'''In Examples'''

acceptable_inputs = ['apple','orange','grape'] 

while True:
    # Using the in keyword to check if something is in the list
    usr_input = input('Enter one of the allowed fruit: ')

    if usr_input in ['1','2','3','4']:
        print("That fruit is allowed!")
        break
    else:
        print('Fruit not found!')
    
my_string = 'Hello world!'
while True:
    # Using the in keyword to check if something is in the list
    usr_input = input('Enter a letter: ')

    if usr_input in my_string:
        print("That letter is allowed!")
        break
    else:
        print('Letter not found!')
        
