'''Try Except Examples'''

my_string = 'Hello'
while True:
    # Creating the Try Except
    try:
        usr_input = int(input('Enter an index to check: '))
        if usr_input == 13:
            raise IndexError
        print(my_string[usr_input])
        break
        
    # Creating the except portion
    # except Exception:
    #     print('An error occured!')
    except IndexError:
        print('That number is is not allowed!')
    # except ValueError:
    #     print('That\'s not a valid number')
    # except (IndexError, ValueError):
    #     print('Invalid input!')