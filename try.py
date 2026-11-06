'''Try Except Exampes'''

my_string = 'Hello'

while True:
    # creating the try except
    
    try:
        usr_input = int(input('Enter an index to check: '))
        print(my_string[usr_input])
        break
    except (IndexError, ValueError):
        print('An unhandled exception has occured.')
    # except IndexError:
    #     print('That index is out of range.')
    # except ValueError:
    #     print('That value is not acceptable.')
    # except Exception:
    #     print('An unhandled exception has occured.')