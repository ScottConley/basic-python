'''Split & Join examples'''

# Splitting a user input
first_name,last_name = input('Enter your first and last name: ').split()[:2]

# Splitting on something thats not a space
my_string = 'joe-schmoe'
joes_name = my_string.split('-')
print(joes_name)

print(first_name)
print(last_name)

#Unpacking a list
num1,num2 = [9,10]
print(num1)
print(num2)

# Multiple Assignment
a,b,c = 1,2,3

# Joining a list into a string 
print('_'.join(joes_name))