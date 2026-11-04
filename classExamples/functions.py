'''Function Examples'''

# Defining a function (Creating a function)
def greeting():
    '''Prints a greeting to the user'''
    print('Hello world!')

# Define a function that recieves an argument
def arg_greeting(name):
    print(f"Hello {name}") 
    
# Define a function that recieves an argument
def mult_arg_greeting(f_name,l_name):
    print(f'Hello, {f_name} {l_name}!')   
    
# Define a function that returns something
def return_greeting():
    first_name = input('Enter a first name: ')
    custom_greeting = f'Hello {first_name}! (from the return_greeting function)'
    
    # Return something out of the function to where it was called
    return custom_greeting

# Creating our 'main' function
def main():
    '''Our main function to call functions/make variables'''
    
    f_name = 'Joe'
    l_name = 'Schmoe'
    
    # Calling a function (Running a function)
    greeting()

    # Calling a function that has an argument
    arg_greeting(f_name)
    
    # Calling a function that has two arguments
    mult_arg_greeting(l_name,f_name)
    
    # Calling our function that has a return
    custom_greeting = return_greeting()
    print(custom_greeting)
    
main()
