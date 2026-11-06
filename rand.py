'''Random examples'''

import random as r

r.seed(788)

print(round(r.uniform(20,40), 2))

ran_num = r.uniform(20,40)

print(f'{ran_num:.2f}')

while True:
    
    usr_input = input('Would you like to roll the dice? ')
    
    if usr_input == 'yes':
        print(r.randint(1,6))
    else:
        break
