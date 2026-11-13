'''Number guessing game module'''

import random
import scoreboard as sb

def num_check() -> int:
    while True:
        try:
            guess = input("Guess the number. It's between 1 and 100! ")
            guess = int(guess)
            if guess == 13:
                raise IndexError
            
            if 1 <= guess <= 100:
                return guess
            print("That's not between 1 and 100!")
                
        except ValueError:
            print("I said number!")
            continue
            
        except IndexError:
            print("That number is NOT allowed.")
            continue
            
def play_game(target: int) -> int:
    count = 0
    while True:
        guess = num_check()
        count += 1

        if guess < target:
            print("That's too low! Try again.")
        elif guess > target:
            print("That's too high! Try again.")
        else:
            print("You guessed it!")
            return count, guess
            
def score(attempts: int, guess: int) -> None:
    initials = input("Please enter your initials: ")
    print(f"The user {initials.upper()} has solved the game in {attempts} tries with a guess of {guess}!")
    return initials

def main() -> None:
    rand_num = random.randint(1, 100)
    print(rand_num)
    total_attempts, guess = play_game(rand_num)
    initials = score(total_attempts, guess)
    sb.main(initials, total_attempts)
    
if __name__ == "__main__":
    main()