'''While Loops Examples'''

# Initializing our counter outside the loop
counter = 0

# # Creating a while loop
# while counter <= 20:
#     counter += 1
#     print(counter)
#     # counter = counter + 1
    
# Infinite while loop
while True:
    counter += 1
    if counter == 13:
        continue
    # Break the loop when counter is equal to 18
    if counter >= 18:
        break
    print(counter)

    