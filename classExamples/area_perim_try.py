'''Area or Perimeter Calculator'''

import math

def main():
    # Creating list of shapes to display
    shapes = ['Square','Circle','Hexagon','Rectangle']
    calculation = ['Area','Perimeter']
    
    while True:
        print(f'Possible shapes: ')

        # Using enumerate to get the index/values to show the user
        for idx,shape in enumerate(shapes,start=1):            
            print(f'Enter {idx} for {shape}')

        # Error handling to check if their inputs are 'in" the allowed choices
        choices = ['1','2','3','4']
        usr_shape = input('\nWhat shape would you like to calculate?: ')
        if usr_shape in choices:
            break
        else:
            print('\nInvalid input\n')
            
    while True:
        print(f'\nPossible choices: ')    
    
        for idx,calc in enumerate(calculation):
            idx += 1
            print(f'Enter {idx} for {calc}')
        usr_calc = input(f'\nWhat do you want to calculate?: ')
        if usr_calc in ['1','2']:
            break
        else:
            print('\nInvalid input')
    
    # Running the proper function
    if usr_shape == '1':
        square(usr_calc)
    elif usr_shape == '2':
        circle(usr_calc)
    elif usr_shape == '3':
        hexagon(usr_calc)
    elif usr_shape == '4':
        rectangle(usr_calc)  

def square(usr_calc):
    ''' Square area/perimeter'''
    
    while True:
        try:
            side = float(input('\nEnter the length of the side: '))
            break
            
        except ValueError:
            print('Error: Please enter a number')

    if usr_calc == '1':
        print(f'\nArea = {side * side}')
    else:
        print(f'\nPerimeter = {side * 4}')    


def rectangle(usr_calc):
    ''' Rectangle area/perimeter'''
    
    while True:
        try:
            side1 = float(input('\nEnter the length of the side: '))
            break
            
        except ValueError:
            print('Error: Please enter a number')
    while True:
        try:
            side2 = float(input('\nEnter the length of the side: '))
            break
            
        except ValueError:
            print('Error: Please enter a number')

    if usr_calc == '1':
        print(f'\nArea = {side1 * side_2}')
    else:
        print(f'\nPerimeter = {(side1 + side2) * 2}')     

def circle(usr_calc):
    '''Circle area/perimeter'''
    
    while True:
        try:
            radius = float(input('\nEnter the radius of the side 1: '))
            break
        except ValueError:
            print('Error: Enter a number')
    
    if usr_calc == '1':
        print(f'\nArea = {math.pi * (radius ** 2)}')
    else:
        print(f'\nPerimeter = {2 * math.pi * radius * 2}')  


def hexagon(usr_calc):
    '''Hexagon area/perimeter'''
    
    while True:
        try:
            side = float(input('\nEnter the length of the side: '))
            break
            
        except ValueError:
            print('Error: Please enter a number')
    
    if usr_calc == '1':
        print(f'\nArea = {((3 * math.sqrt(3)) / 2) * (side ** 2)}') 
    else:
        print(f'\nPerimeter = {6 * side}')

if __name__ == '__main__':
    main()
    