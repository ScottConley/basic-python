'''Indexing and Slicing Examples'''

my_string = 'This is my string to index'`

# # Getting the length of an iterable
# print(len(my_string))

# Indexing a string
print(my_string[5])

my_list = ['This','is','my','list','to','index']

# Indexing a list
print(my_list[-1])

# Using split to create a list from a string
my_list = my_string.split()

# Changing 'string' to 'list' in the list
my_list[3] = 'list'

print(my_list)

# Slicing a string - [start:stop:step] stop not inclusive 
print(my_string[:5])

#Slicing a list
print(my_list[::2])

# For Loops, stripping, looping over a slice