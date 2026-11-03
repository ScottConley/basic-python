'''For loop practice'''

my_string = 'String to loop'
list_of_string = my_string.split()

my_list = ["List", "to", "loop"]

# Creating a for loop over a string

print(len(my_string))

i = 1

for char in my_string:
    #print(i, ": ", char)
    print(f'{i}: {char}')
    i+=1
    
i = 1
    
for item in list_of_string:
    print(f'{i}: {item}')
    i+=1
    
# Looping over slices

i = 1

for char in my_string[:5:1]:
    print(f'{i}: {char}')
    i+=1

i = 1

for char in my_string[7:9:1]:
    print(f'{i}: {char}')
    i+=1
    
i = 1

for char in my_string[10:14:1]:
    print(f'{i}: {char}')
    i+=1
    
# Looping over list sclices

i = 1

for item in list_of_string[:1:1]:
    print(f'{i}: {item}')
    i+=1

i = 1

for item in list_of_string[0:2:1]:
    print(f'{i}: {item}')
    i+=1
    
i = 1

for item in list_of_string[2:3:1]:
    print(f'{i}: {item}')
    i+=1

i = 1

for item in list_of_string[0:3:2]:
    print(f'{i}: {item}')
    i+=1
    
i = 1

for item in list_of_string[1:3:2]:
    print(f'{i}: {item}')
    i+=1
    
# def shuvit():

#Loop over a List and change the elements in the list

all_caps_list = []
i = 1

for item in list_of_string:
    all_caps_list.append(item.upper())
    print(all_caps_list[i-1:i:1])
    print(all_caps_list[])
    i+=1
    
print(all_caps_list)
    