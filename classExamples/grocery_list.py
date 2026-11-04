grocery_list = []

# Making list to extend
items_to_add = ['Milk','Eggs','Bread','Yogurt']

# Adding all grocery items to our list
grocery_list.extend(items_to_add)

grocery_list.insert(0,'Butter')
# # index = grocery_list.index('Eggs')
# removed_items = grocery_list.pop(grocery_list.index('Eggs'))
# print(removed_items)

# Changing a value based off the index position.
grocery_list[2] = 'Whole Wheat Bread'

user_addition = input('Enter a item to add: ').capitalize()
grocery_list.append(user_addition)
grocery_list.sort()
print(grocery_list)

                    

