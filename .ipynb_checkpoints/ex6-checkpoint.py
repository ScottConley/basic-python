'''Project Euler'''

# Find the sum of all multiples of 3 or 5 below one thousand

# multiples = []
s = 0
usr_input = input('Please enter your Euler Multiples target number (default: 999): ')
target = int(usr_input or 999)

for i in range(1,target):
    if i % 3 == 0 or i % 5 == 0:
        # multiples.append(i)
        s += i
        
print(f'The target number is {target}.')
print(f'The sum of the multiples of three and five below this target is: {s}') # {sum(multiples)}

# This ones just for fun

for i in range(1,100): print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

print(sum([x for x in range(1, 999) if i % 3 == 0 or i % 5 == 0]))