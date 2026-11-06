'''Indexing and Slicing'''

my_string = 'This is my string to index'
my_list = ['This', 'is', 'my', 'list', 'to', 'index']

print(my_list[-2])

# Indexing a string

my_indexed_string = my_string.index('string')

print(my_string)
print(my_string[1])
print(my_string[len(my_string)-1])
print(my_string[-1].capitalize())
print(my_indexed_string)
print(len(my_string))

# Indexing a list

my_indexed_list = my_list.index('list')

print(my_list)
print(my_list[2])
print(my_list[len(my_list)-1])
print(my_list[-1].capitalize())
print(my_indexed_list)
print(len(my_list))

# Splitting a string

my_split_string = my_string.split()

print(my_split_string)
print(my_string.split())

my_split_string[3] = 'index'
print(my_split_string)

# Slicing a string - [start:stop:step] stop not inclusive

print(my_string[:5])
print(my_string[5:])
print(my_string[::2])
print(my_string[::-1])

# Slicing a list

print(my_list[:3])
print(my_list[3:])
print(my_list[::2])
print(my_list[::-1])

# For next exercise looking into...
# For Loops, stripping, looping over a slice