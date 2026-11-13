'''Pizza Toppings'''

toppings = {
    'pepperoni' : 1.00,
    'mushrooms' : 0.80,
    'green peppers' : 0.80,
    'black olives' : 0.80,
    'pineapple' : 0.90,
    'spinach' : 0.75,
    'onions' : 0.70,
    'jalapenos' : 0.85,
    'bacon' : 1.20,
    'chicken' : 1.10,
    'ham' : 1.15
}

sizes = {
    'small' : 12.50,
    'medium' : 13.50,
    'large' : 14.50,
    'xl' : 15.50
}

options = {
    'deep dish' : 2.50,
    'extra cheese' : 2.00
}

def get_string(prompt, dict_name):
    while True:
        try:
            string = str(input(prompt)).lower()
            if string.isdigit():
                print('Strings only. Be cool.')
                continue
            elif string in ['done', 'none']:
                print('I\'ve got your selection as follows: ')
            elif string not in dict_name.keys():
                print(f'That\'s not in the list...')
                continue
            return string
        except ValueError:
            print('Please enter a string. Be cool.')
            
def get_restart(prompt_restart):
    while True:
        try:
            string = str(input(prompt_restart)).lower()
            if string.isdigit():
                print('Strings only. Be cool.')
                continue
            elif string not in ['yes', 'no']:
                print('That\'s not an option!')
                continue
            elif string in ['yes', 'no']:
                print(f'Thank you for your order!')
            return string
        except ValueError:
            print('Please enter a string. Be cool.')

def get_toppings(welcome, prompt_toppings, selected_toppings):
    print(welcome)
    
    for topping, price in enumerate(toppings.items()):
        print(f'{topping}: {price}')
        
    while True:
    
        topping_selection = get_string(prompt_toppings, toppings)

        if topping_selection.lower() == 'done':
            break
        
        selected_toppings.append(topping_selection)
        
    print(", ".join(selected_toppings))
    
    return selected_toppings

def get_size(prompt_size, selected_size):
    print(prompt_size)
    
    for size, price in enumerate(sizes.items()):
        print(f'{size}: {price}')
        
    while True:
    
        size_selection = get_string(prompt_size, sizes)
            
        selected_size.append(size_selection)
        
        if size_selection in sizes:
            print(f'You\'ve selected {size_selection}')
            break
                    
    return selected_size

def get_option(prompt_option, selected_option):
    print(prompt_option)
    
    for option, price in enumerate(options.items()):
        print(f'{option}: {price}')
        
    while True:
    
        option_selection = get_string(prompt_option, options)

        if option_selection.lower() == 'none':
            break
            
        selected_option.append(option_selection)
        
        if option_selection in options:
            print(f'You\'ve select {option_selection}')
            break
                    
    return selected_option

def total_calc(wrap_up, prompt_total, selected_toppings, selected_size, selected_option):
    
    topping_price = [toppings[k] for k in toppings if k in selected_toppings]
    
    size_price = [sizes[k] for k in sizes if k in selected_size]
    
    option_price = [options[k] for k in options if k in selected_option]
    
    wrap_up_list = [*selected_toppings, *selected_size, *selected_option]
    
    print(f'{wrap_up}{", ".join(wrap_up_list)}')
    
    calc_list = [*topping_price, *size_price, *option_price]
    
    print(f'{prompt_total}{round(sum(calc_list), 2)}')

def main():
    while True:
        
        selected_toppings = []
        selected_size = []
        selected_option = []

        total = 0

        welcome = 'Welcome to the Low-Cal Calzone Zone! Please observe the following options:'
        prompt_toppings = 'Enter a topping (\'done\' when you\'re finsished): '
        get_toppings(welcome, prompt_toppings, selected_toppings)

        prompt_size = 'What size of pizza would you like?: '
        get_size(prompt_size, selected_size)

        prompt_option = 'What option would you like? (You may also enter \'none\'): '
        get_option(prompt_option, selected_option)

        wrap_up = 'You\'re total selection is as follows: '
        prompt_total = 'You\'re total is: $'
        total_calc(wrap_up, prompt_total, selected_toppings, selected_size, selected_option)
        
        prompt_restart = 'Are you satisfied with your order? (yes or no) '
        
        restart = get_restart(prompt_restart)
        if restart == 'yes':
            break
        else:
            continue

if __name__ == '__main__':
    main()