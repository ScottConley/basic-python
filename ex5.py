'''String Split & Joine Exercise'''

# ---------------------------------------
# Instructions:
# - Work through each Part in order.
# - Replace each TODO with working code.
# - Run the file after each part to see your progress.
# - No external libraries needed. Use built-in string methods: .split(), .join(), .strip()
#
# Tips:
# - split() -> turns a string into a list of pieces.
# - join()  -> turns a list of strings back into a single string (use the separator on the left).
# - strip() -> removes leading/trailing whitespace.
# - len()   -> returns the number of items in an object
#
# Example:
#   "a b  c".split()           -> ["a","b","c"]
#   ", ".join(["a","b","c"])   -> "a, b, c"


print("=== Part 1: Words from a sentence ===")
sentence = "Python makes string work feel pretty friendly."
# TODO 1a: Split sentence into words (on spaces) and store in a list called words.
# TODO 1b: Print how many words there are.
# TODO 1c: Print the first and last word.
# Hints: .split() with no args splits on any whitespace.

# Your code here

words = sentence.split()
print(f'1a: {words}')
print(f'1b: {len(words)}')
print(f'1b: {words[::6]}')

print("\n=== Part 2: Clean a comma-separated list ===")
raw_items = " apples,  bananas,grapes ,  mangoes ,pineapple  "
# Goal: turn into "Apples | Bananas | Grapes | Mangoes | Pineapple"
# Steps:
#   - Split on "," to get a rough list.
#   - Strip whitespace from each piece.
#   - Capitalize each item
#   - Re-join with " | " as the separator.
# TODO 2: Implement the above and print the final string.Hmm, I'm a little disappointed that the only way to make Altergeist strong enough to fight the top tier is so much reliance on two other archetypes. I'd hate with something that's basically just "good stuff pile". That has absolutely no style :(Hmm, I'm a little disappointed that the only way to make Altergeist strong enough to fight the top tier is so much reliance on two other archetypes. I'd hate with something that's basically just "good stuff pile". That has absolutely no style :(Hmm, I'm a little disappointed that the only way to make Altergeist strong enough to fight the top tier is so much reliance on two other archetypes. I'd hate with something that's basically just "good stuff pile". That has absolutely no style :(Hmm, I'm a little disappointed that the only way to make Altergeist strong enough to fight the top tier is so much reliance on two other archetypes. I'd hate with something that's basically just "good stuff pile". That has absolutely no style :(Hmm, I'm a little disappointed that the only way to make Altergeist strong enough to fight the top tier is so much reliance on two other archetypes. I'd hate with something that's basically just "good stuff pile". That has absolutely no style :(

# Your code here

rough_list = raw_items.split(',')
print(f'2a: {rough_list}')

stripped_list = [item.strip() for item in rough_list]
print(f'2b: {stripped_list}')

caps_list = []
i = 1

for item in stripped_list:
    caps_list.append(item.capitalize())
    print(caps_list[i-1:i:1])
    i+=1
    
print(f'2c: {caps_list}')
join_list = ' | '.join(caps_list)
print(f'2d: {join_list}')

print("\n=== Part 3: Parse a profile string ===")
profile = "jordan:smith:jordan.smith@example.com"
# Format is "first_name:last_name:email".
# Goal output: "Jordan Smith <jordan.smith@example.com>"
# TODO 3: Split profile by ":", capitalize the names, and then build the f string. Print it.

# Your code here

first_name, last_name, email = profile.split(':')
print(f'Split begin: {first_name}, {last_name}, {email}')
name = ' '.join([first_name.capitalize(), last_name.capitalize()])
print(f'Goal Output: {name} <{email}>')



print("\n=== Part 4: User input to hyphen-joined toppings ===")
# Ask the user for pizza toppings separated by spaces, e.g. "olives mushrooms pepperoni"
# Then:
#   - Split into a list of toppings.
#   - Strip each (in case the user typed "  olives ").
#   - Lowercase each topping for consistency.
#   - Sort the list alphabetically.
#   - Join back into one string using " - ".
# TODO 4: Implement the above and print the final hyphen-joined string.

# Your code here

toppings = input('Please tell me all the pizza toppings you like. Use spaces to separate them!: ')

split_top = toppings.split()
print(f'4a: {split_top}')

strip_top = toppings.strip()
print(f'4b: {strip_top}')

lower_top = [item.lower() for item in split_top]
print(f'4c: {lower_top}')

lower_top.sort(key = str.lower)
print(f'4d: {lower_top}')

string_top = '-'.join(lower_top)
print(f'4e: {string_top}')