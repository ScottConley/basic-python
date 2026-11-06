'''Fibonacci Number'''

fib = []
fib_evens = []
limit = 4000000

a, b = 0, 1

while b < limit:
    fib.append(b)
    a, b = b, a + b
    
    if b % 2 == 0:
        fib_evens.append(b)
    
print(f'Here\'s the Fibonnaci Sequence up to 4000000: {fib}\n')
print(f'Here\'s the Fibonnaci Evens up to 4000000: {fib_evens}\n')
print(f'Here\'s the Fibonnaci Total up to 4000000: {sum(fib_evens)}\n')