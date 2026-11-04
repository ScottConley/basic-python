'''Euler 1'''

print(sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]))

total = 0
for num in range(1,1000):
    if num % 3 == 0:
        total += num
    elif num % 5 == 0:
        # total = total + num
        total += num
print(total)