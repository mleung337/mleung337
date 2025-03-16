# Matthew Leung

import random

print('\nRock, Paper, Scissors!')
win = 0
loss = 0
tie = 0
print(f'{win} wins, {loss} losses, & {tie} ties.')
rock = 0
paper = 1
scissors = 2

while True:
    opponent_choice = random.randint(0,2)
    player_choice = input('\nEnter your move: (r)ock/(p)aper/(s)cissors/(q)uit ')

    if player_choice == 'r':

        if opponent_choice == scissors:
            print('\nYou won!')
            win += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

        elif opponent_choice == paper:
            print('\nYou lost!')
            loss += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

        elif opponent_choice == rock:
            print('\nWe tied!')
            tie += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

    elif player_choice == 'p':

        if opponent_choice == rock:
            print('\nYou won!')
            win += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

        elif opponent_choice == scissors:
            print('\nYou lost!')
            loss += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

        elif opponent_choice == paper:
            print('\nWe tied!')
            tie += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

    elif player_choice == 's':

        if opponent_choice == paper:
            print('\nYou won!')
            win += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

        elif opponent_choice == rock:
            print('\nYou lost!')
            loss += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')

        elif opponent_choice == scissors:
            print('\nWe tied!')
            tie += 1
            print(f'{win} wins, {loss} losses, & {tie} ties.')
        
    elif player_choice == 'q':
        print('\nQuitting...')
        break
    else:
        print('\nInvalid input.')
        continue
