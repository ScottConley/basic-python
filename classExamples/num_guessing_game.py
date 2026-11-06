"""Number guessing game - A game where the user guesses a number between 1 and 100"""

import random

def main():
    
    #assigns a random winning number to a variable
    winning_num = random.randint(1,100)
    
    # Call my guessing_game function and send in the winning_num
    score, initials = guessing_game(winning_num)
    
    # Converting my score into a traditional score
    score = 100 - score
    print(f'{initials.upper()} wins! Your score is {score}')
    
def guessing_game(winning_num):
    """Gets guesses from the user until they match winning number """
    
    guess_counter = 0
    
    # Loop to track their guesses and make sure they are entering digits
    while True:
        # Testing purposes
        print(winning_num)
        guess = input('Guess a number between 1 and 100: ')        

        # Checks if the input is an integer and casts it.
        if guess.isdigit():
            guess = int(guess)
        else:
            print('Error: Please enter a number between 1 and 100\n')
            continue
        
        # Checks if guess is within range
        if guess < 1 or guess > 100:
            print('Error: Please enter a number between 1 and 100\n')
            continue
        
        # Increases the guess counter for each guess and checks for win condition
        else:
            guess_counter += 1
            if guess > winning_num:
                print('Too high! Try again\n')
            elif guess < winning_num:
                print('Too low! Try again\n')
            else:
                initials = input('Enter your initials: ')
                return guess_counter, initials
            
if __name__ == '__main__':
    main()
