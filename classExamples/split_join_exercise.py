'''String Split & Join Exercise'''
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

#
print("=== Part 1: Words from a sentence ===")
sentence = "Python makes string work feel pretty friendly."
# TODO 1a: Split sentence into words (on spaces) and store in a list called words.
# TODO 1b: Print how many words there are.
# TODO 1c: Print the first and last word.
# Hints: .split() with no args splits on any whitespace.

words = sentence.split()
print(f'There are {len(words)} words.')
print(f'First word: {words[0]} - Last word: {words[-1]}')
# print(words[0],words[-1])


print("\n=== Part 2: Clean a comma-separated list ===")
raw_items = " apples,  bananas,grapes ,  mangoes ,pineapple  "
# Goal: turn into "Apples | Bananas | Grapes | Mangoes | Pineapple"
# Steps:
#   - Split on "," to get a rough list.
#   - Strip whitespace from each piece.
#   - Capitalize each item
#   - Re-join with " | " as the separator.
# TODO 2: Implement the above and print the final string.

fruit = raw_items.split(',')

# List Comprehension
# processed_fruit = [x.strip().capitalize() for x in fruit]

# final_string = ' | '.join(processed_fruit)

processed_fruit = []

for element in fruit:    processed_fruit.append(element.strip().capitalize())
    
final_string = ' | '.join(processed_fruit)

print(final_string)


print("\n=== Part 3: Parse a profile string ===")
profile = "jordan:smith:jordan.smith@example.com"
# Format is "first_name:last_name:email".
# Goal output: "Jordan Smith <jordan.smith@example.com>"
# TODO 3: Split profile by ":", capitalize the names, and then build the f string. Print it.

# Multiple assignment to unpack a list
first_name, last_name, email = profile.split(':')

# profile[0] = profile[0].capitalize()
# profile[1] = profile[1].capitalize()

print(f'{first_name.capitalize()} {last_name.capitalize()} <{email}>')


print("\n=== Part 4: User input to hyphen-joined toppings ===")
# Ask the user for pizza toppings separated by spaces, e.g. "olives mushrooms pepperoni"
# Then:
#   - Split into a list of toppings.
#   - Strip each (in case the user typed "  olives ").
#   - Lowercase each topping for consistency.
#   - Sort the list alphabetically.
#   - Join back into one string using " - ".
# TODO 4: Implement the above and print the final hyphen-joined string.

usr_toppings = [x.strip().lower() for x in input('What toppings do you want? ').split()]

# usr_toppings =  input('What toppings do you want? ').split()

# processed_toppings = []

# for topping in usr_toppings:
#     processed_toppings.append(topping.strip().lower())

# processed_toppings.sort()
usr_toppings.sort()

str_toppings = ' - '.join(usr_toppings)
print(str_toppings)














# list_prof = profile.split(':')
# list_prof[0] = list_prof[0].capitalize()
# list_prof[1] = list_prof[1].capitalize()

# print(f'{list_prof[0]} {list_prof[1]} <{list_prof[2]}>')
