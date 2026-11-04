'''List Comprehension Examples'''

# Making a list of numbers from 1 through 10
num_list = list(range(1,11))

# Using a for loop
for_loop_list = []
for num in range(1,11):
    for_loop_list.append(num)

# Using list comprehension
list_comp_list = [num for num in range(1,11)]

# Doubled list
doubled_list = [num * 2 for num in list_comp_list]

# Squared List
squared_list = [num ** 2 for num in num_list]

# Even list
even_list = [x for x in num_list if x % 2 == 0]

print(num_list)
print(for_loop_list)
print(list_comp_list)
print(doubled_list)
print(squared_list)
print(even_list)