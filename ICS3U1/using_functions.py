# Matthew Leung

import random

def numGame():
    '''Sets variables to original values'''
    global attempts, num_max, num_min, num_random
    attempts = 0
    num_max = 100
    num_min = 1
    num_random = random.randint(1, 100)
    
def incorrectGuess():
    '''Displays when guessed high, adds to attempts'''
    global attempts, num_guess, num_max, num_min, num_random
    attempts += 1
    if num_guess > num_random:
        num_max = num_guess
        print('\nGuess lower.')
    elif num_guess < num_random:
        num_min = num_guess
        print('\nGuess higher.')

def correctGuess():
    '''Displays when guessed correct, adds to attempts'''
    global attempts
    attempts += 1
    print(f'\nCorrect number.\nTook {attempts} attempts.')

def invalidInput():
    '''Displays invalid input for invalid input'''
    print('\nInvalid input.')

def outOfRange():
    '''Displays when input guess is out of range'''
    print('\nPlease keep your guesses within range.')

def close():
    '''Closes program'''
    print('\nQuitting...')
    raise SystemExit

def retry():
    '''Allows user to play again'''
    while True:
        retry = input('\nReplay? (y)es/(n)o ')
        if retry == 'y':
            numGame()
            break
        elif retry == 'n':
            close()
        else:
            invalidInput()
            continue

numGame()

while True:
    num_guess = input(f'\nGuess a number between {num_min} to {num_max}: ')

    try:
        int(num_guess)
        num_guess = int(num_guess)

        if num_guess > num_max or num_guess < num_min:
            outOfRange()

        elif num_guess != num_random:
            incorrectGuess()
            
        elif num_guess == num_random:
            correctGuess()
            retry()

    except ValueError:
        invalidInput()
        continue
