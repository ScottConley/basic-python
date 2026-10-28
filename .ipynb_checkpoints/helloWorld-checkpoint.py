'''This pyfile prints a greeting to the user'''

print('Hello, World!\n')

for i in range(5):
    print('Hello, ',i+1)
    
# This was a fun file to write!

# Creating Variables

first_name = 'Scott'
last_name = 'Conley'

full = first_name+', '+last_name

print('Hello, ' + first_name + '!')

# Utilize an f-string
print(f'Hello, {first_name} {last_name}!')

#utilize commas
print("Hello ", first_name, last_name)

print(full.upper())

print(full.lower())

print(full.split(", "))

print("The amount of times \"t\" appears in my name is... ",full.count("t"))