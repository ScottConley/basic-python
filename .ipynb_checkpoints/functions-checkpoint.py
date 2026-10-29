'''Function Examples'''

def hello():
    print('Hello, World!')
    
def goodbye():
    print('Goodbye, friend!')
    
greet = input('Hello? Or Goodbye? ')
    
def arg_greet(greet):
    print(greet)
    
def multi_arg_greet(first_name, last_name):
    print(f'Hello, {first_name} {last_name}')
    
arg_greet('Hi!')

def main():
    '''Our main function to call functions/make variables'''
    first_name = 'Joe'
    last_name = 'Conley'
    
    arg_greet(first_name)
    
    multi_arg_greet(first_name, last_name)

    if greet == 'Hello':
        hello()
    elif greet == 'Goodbye':
        goodbye()
    else:
        print('ok')
        
main()