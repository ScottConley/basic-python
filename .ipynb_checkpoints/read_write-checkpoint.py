'''read and write to files'''

# Reading a text file
with open('example.txt', 'r') as f:
    # printing first line of text
#     print(f.readline())
#     print(f.readline()) # This will read line 2
    
    # printing all lines as a string
    # print(f.read())
    
    # print each line as an element of a list
    # print(f.readlines())
    
    # printing each line as element of list without \n
    # print(f.read().splitlines())
    
    # list comp method
    # rem_n = [x.strip() for x in f.readlines()]
    # print(rem_n)