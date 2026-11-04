'''For loop examples'''

my_string = 'String to loop'
list_of_str = my_string.split()

# Creating a For loop over a string
print(len(my_string))
      
counter = 1
# I want every loop to say Character 1: (character here)
for char in my_string:
    print(f'Character {counter}: {char}')
    counter += 1  # counter = counter + 1
    
print(list_of_str)
# For loop over a list
for element in list_of_str:
    print(element)

# For loop over a slice
for char in my_string[:6]:
    print(char)

# New empty list to recieve changed list elements
all_caps_list = []

# Loop over a list and change the elements in the list
for element in list_of_str:
    all_caps_list.append(element.upper())
    
print(all_caps_list)

# For loop over a range
for num in range(1,21):
    if num == 13:
        continue
    print(num)
    


