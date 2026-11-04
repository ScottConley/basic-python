num_list = [x for x in range(1,11)]

doubled_list = [x*2 for x in num_list]

squared_list = [x**2 for x in num_list]

print(num_list)
print(doubled_list)
print(squared_list)

#even list

even_list = [x for x in num_list if x % 2 == 0]
print(even_list)