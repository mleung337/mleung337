# Matthew Leung

import random

attempts = 0
max_number = 100
min_number = 1
random_number = random.randint(1, 100)

while True:
    
    number_guess = input(f'\nFrom {min_number} to {max_number}, guess the number. ')

    try:
        int(number_guess)
        number_guess = int(number_guess)

        if number_guess >= max_number or number_guess <= min_number:
            print('\nPlease keep your guesses within the range.')
            continue

        elif number_guess > random_number and number_guess < max_number:
            attempts += 1
            max_number = number_guess
            print('\nGuess lower.')

        elif number_guess < random_number and number_guess > min_number:
            attempts += 1
            min_number=number_guess
            print('\nGuess higher.')

        elif number_guess == random_number:
            attempts += 1
            print(f'\nCorrect number. \nTook {attempts} attempts.')

            while True:
                retry = input('\nReplay? (y)es/(n)o ')

                if retry == 'y':
                    attempts = 0
                    max_number = 100
                    min_number = 1
                    random_number = random.randint(1, 100)
                    break

                elif retry == 'n':
                    print('\nQuitting...')
                    raise SystemExit

                else:
                    print('\nInvalid input.')
                    continue

        else:
            print('\nInvalid input.')
            continue

    except ValueError:
        print('\nInvalid input.')
        continue
