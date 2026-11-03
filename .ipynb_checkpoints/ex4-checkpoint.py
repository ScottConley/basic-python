'''Pythagorean Theorem Exercise'''

import math as mth

def hypotenuse(side_a, side_b):
    c = mth.sqrt(side_a ** 2 + side_b ** 2)
    return c
    
def main():
    side_a = float(input('Please give me side a: '))
    side_b = float(input('Please give me side b: '))
    
    hyp = hypotenuse(side_a, side_b)
    
    print(f'Your hypotenuse is {hyp}')
    
main()