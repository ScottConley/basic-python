'''Num guessing game'''

import random

def num_guessing_game(win_num):
    '''Runs the game'''
    
    guess_counter = 0
    while True:
        try:
            guess = int(input('\nEnter a number between 1 and 100: '))
            if guess > 100 or guess < 1:
                raise IndexError
            elif guess < win_num:
                print('Guess too low')
                guess_counter += 1
            elif guess > win_num:
                print('Guess too high')
                guess_counter += 1
            else:
                initials = input('You got it! Enter your initials: ')
                score = 100 - guess_counter
                return score, initials
        except ValueError:
            print("That's not a numerical value")
        except IndexError:
            print('Guess out of range')
            
            
def main():    
    # Intializing our winning number
    win_num = random.randint(1,100)
    score, initials = num_guessing_game(win_num)
    print(f"{initials}'s score is {score}!")
                                    
if __name__ == '__main__':
    main()
