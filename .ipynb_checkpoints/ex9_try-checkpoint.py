'''Area or Perimeter Exercise'''

import math

def get_choice(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        for option in valid_options:
            if user_input == option or user_input == option[0]:
                return option[0]
        print(f"Invalid Choice. Please choose from: {', '.join(valid_options)}")
        
def main():
    print("--- Geometry Calculator ---")
    calc_type = get_choice(
        "Would you like to measure (a)rea or (p)erimeter?\n> ", 
        ['area', 'perimeter']
    )
    
main()