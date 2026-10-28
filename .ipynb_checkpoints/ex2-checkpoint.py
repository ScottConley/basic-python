'''The Crocery Store Exercise'''

my_grocery_list = []

for i in ("Milk", "Eggs", "Bread", "Yogurt"):
    my_grocery_list.append(i)

print(my_grocery_list)

my_grocery_list.insert(0, "Butter")

print(my_grocery_list)

my_grocery_list[2] = "Whole Wheat Bread"

print(my_grocery_list)

new_item = input("Please add an item to the grocery list: ")

my_grocery_list.append(new_item)

print(f'Here\'s the final list! {my_grocery_list}')

my_grocery_list.sort(key = str.lower)

print(my_grocery_list)