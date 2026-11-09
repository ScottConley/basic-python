'''Area or Perimeter Exercise'''

import math

def usr_calc_input():
    while True:
        try:
            params = ['area', 'a', 'perimeter', 'p']
            usr_calc_input = input("Would you like to measure area or perimeter?\n")
            usr_calc_input = str(usr_calc_input)
            
            if usr_calc_input.lower() not in params:
                raise IndexError
            
            if usr_calc_input.lower() in params:
                print("You got it!")
                usr_calc_input = usr_calc_input[0:1].lower()
                return usr_calc_input
            
        except ValueError:
            print("It's supposed to be words.")

        except IndexError:
            print("That's not an acceptable answer")
            
def usr_shape_input():
    while True:
        try:
            params = ['square', 's', 'rectangle', 'r', 'circle', 'c', 'hexagon', 'h']
            print("What shape would you like to measure?")
            usr_shape_input = input("Your options are square, rectangle, circle, or hexagon.\n")
            
            if usr_shape_input.lower() not in params:
                raise IndexError
            
            if usr_shape_input.lower() in params:
                print("Sounds good!")
                usr_shape_input = usr_shape_input[0:1]
                return usr_shape_input

        except IndexError:
            print("That's not an acceptable answer")
            
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Measurements must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")
            
def usr_shape_calc(calc_input, shape_input):
    if shape_input == 's':
        side = get_float("Please enter the side length.\n")
        if calc_input == 'a':
            print(f'The area of the square is: {side ** 2}')
        else:
            print(f'the Perimeter of the square is: {4 * side}')

    elif shape_input == 'r':
        length = get_float("Please enter the length.\n")
        width = get_float("Please enter the width.\n")
        if calc_input == 'a':
            print(f'The area of the rectangle: {length * width}')
        else:
            print(f'The perimeter of the rectangle: {2 * length + 2 * width}')

    elif shape_input == 'c':
        radius = get_float("Please enter the radius.\n")
        if calc_input == 'a':
            print(f'The area of the circle is: {math.pi * (radius ** 2):.2f}')
        else:
            print(f'The circumference of the circle is: {math.pi * 2 * radius:.2f}')

    elif shape_input == 'h':
        side = get_float("Please enter the side length.\n")
        if calc_input == 'a':
            area = (3 * math.sqrt(3)/2) * (side ** 2)
            print(f'The area of the hexagon is: {area:.2f}')
        else:
            print(f'The perimeter of the hexagon is: {6 * side}')
                  
def main() -> None:
    calc_input = usr_calc_input()
    shape_input = usr_shape_input()
    usr_shape_calc(calc_input, shape_input)
                
if __name__ == "__main__":
    main()