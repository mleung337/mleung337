# Matthew Leung

import random
import string
import time

# All + 1s used in program are to account for off by one nature of Python

# Print rules of the game

print('LETTER CRUSH\n\nRules of the game:\n1. Three or more adjacent letters of the same kind are removed.\n2. Cleared squares are filled in by above squares.\n3. Empty squares are filled in by random letters.\n4. One point is earned for every letter removed - reach 100 points!\n5. Have fun!')

# Define size of grid

def gridSize():

    '''Defines size for grid'''

    while True:
        user_input = input('\nBetween a grid size minimum of 5 and a grid size maximum of 10, what size would you like? ')

        try:
            int(user_input)
            user_input = int(user_input)
            
            if user_input >= 5 and user_input <= 10:
                return user_input

        except ValueError:
            print('\nInvalid input.')
            continue

size = gridSize()

# Create grid values

objects_list = ['Q', 'R', 'S', 'T', 'U']

def gridValues():
    
    '''Defines values for grid'''
    
    def rowValues():
        
        '''Defines values per row'''
        
        random_object = random.choice(objects_list)
        row = [random_object]

        while len(row) != size:
            random_object = random.choice(objects_list)
            row.append(random_object)

        return row

    grid = [rowValues()]

    while len(grid) != size:
        grid.append(rowValues())

    return grid

original_grid = gridValues()
copied_grid = list(original_grid)
points = 0

# Print grid values

alphabet = string.ascii_uppercase
column_letters = list(string.ascii_uppercase[:size])
row_numbers = list(range(size + 1))

def printGrid():
    
    '''Prints current grid values'''
    
    # Number of rows
    row_number = size
    lines = []

    while len(lines) != size + 1:
        lines.append('+')
    
    for row in original_grid:

        if row_number >= 10:
            print('\n')
            print(f"    {'———'.join(lines)}\n {row_number} | {' | '.join(row)} |")
            row_number -= 1

        else:
            print(f"    {'———'.join(lines)}\n {row_number}  | {' | '.join(row)} |")
            row_number -= 1
        
    print (f"    {'———'.join(lines)}\n      {'   '.join(column_letters)}")

# Accept user input and swaps both objects

def objectSwap():

    '''Checks which square is selected'''

    global points
    
    def objectSelect():

        '''Accepts user input to check which square is selected'''
        
        while True:
            user_input = input('\nLetter first, then number.\nre(p)rint / (c)ancel / (q)uit\nPick a slot: ')

            if user_input == 'c':
                return user_input

            elif user_input == 'p':
                printGrid()
                continue

            elif user_input == 'q':
                print('\nQuitting game...')
                raise SystemExit

            if size >= 10:

                if len(user_input) == 3:
                    number = user_input[1:3]
                    letter = user_input[0].capitalize()

                    try:
                        int(number)
                        number = int(number)
                        
                        if number in row_numbers:

                            if letter in column_letters:
                                numberlist_index = 0
                    
                                for numbers in row_numbers:
                            
                                    if numbers != number:
                                        numberlist_index += 1
                                
                                letterlist_index = 0
                            
                                for letters in column_letters:
                                
                                    if letters != letter:
                                        letterlist_index += 1
                                    
                                selected_object = copied_grid[size - numberlist_index][letterlist_index]
                                return letterlist_index, size - numberlist_index, selected_object, user_input

                            else:
                                print('\nInvalid input.')

                        else:
                            print('\nInvalid input.')
                            continue

                    except ValueError:
                        print('\nInvalid input.')
                        continue
                
                else:
                    print('\nInvalid input.')
                    continue

            else:

                if len(user_input) == 2:
                    number = user_input[1]
                    letter = user_input[0].capitalize()

                    try:
                        int(number)
                        number = int(number)
                        
                        if number in row_numbers:

                            if letter in column_letters:
                                numberlist_index = 0
                    
                                for numbers in row_numbers:
                            
                                    if numbers != number:
                                        numberlist_index += 1

                                    else:
                                        break
                                
                                letterlist_index = 0
                            
                                for letters in column_letters:
                                
                                    if letters != letter:
                                        letterlist_index += 1

                                    else:
                                        break
                                    
                                selected_object = copied_grid[size - numberlist_index][letterlist_index]
                                return letterlist_index, size - numberlist_index, selected_object, user_input

                            else:
                                print('\nInvalid input.')

                        else:
                            print('\nInvalid input.')
                            continue

                    except ValueError:
                        print('\nInvalid input.')
                        continue
                
                else:
                    print('\nInvalid input.')
                    continue

    def swap():

        '''Swaps selected squares'''

        copied_grid[first_values[1]][first_values[0]] = second_values[2]
        copied_grid[second_values[1]][second_values[0]] = first_values[2]
        original_grid = list(copied_grid)
        
    while True:
        first_values = objectSelect()

        if first_values == 'c':
            print('\nNothing selected.')
            continue

        print('\nNow pick one to swap with.')
        second_values = objectSelect()
        
        if second_values == 'c':
            print('\nCancelling current selection...')
            continue
        
        if first_values[3] == second_values[3]:
            print('\nInvalid input. Same slot.')
            continue

        elif first_values[1] != second_values[1] and first_values[0] != second_values[0]:
            print('\nInvalid input. Diagonal.')
            continue
        
        if first_values[1] + 1 == second_values[1] or first_values[1] - 1 == second_values[1]:
            swap()
            break
            
        else:
            
            if first_values[1] == second_values[1]:

                if first_values[0] + 1 == second_values[0] or first_values[0] - 1 == second_values[0]:
                    swap()
                    break
            
                else:
                    print('\nInvalid input. Too far.')
                    continue

            else:
                print('\nInvalid input. Too far.')
                continue
        

# Remove same adjacent objects

def objectCrush():

    '''Checks and removes horizontal adjacency, then vertical adjacency'''

    global points

    # Shifts down above objects

    def objectFill():

        '''Shifts down objects from top'''

        if times_removed > 0:

            while True:
                count = 0
                        
                for index, row in enumerate(copied_grid):
                                        
                    for index2, objects in enumerate(row):

                        if copied_grid[index][index2] == ' ' and copied_grid[index - 1][index2] != ' ' and index - 1 >= 0:
                            copied_grid[index][index2] = copied_grid[index - 1][index2]
                            copied_grid[index - 1][index2] = ' '
                            count += 1

                if count == 0:
                    break
                
        original_grid = list(copied_grid)
        
    # Fill in missing objects

    def objectReplace():

        '''Replaces empty slots'''

        for index, row in enumerate(copied_grid):

            for index2, objects in enumerate(copied_grid):

                if copied_grid[index][index2] == ' ':
                    copied_grid[index][index2] = random.choice(objects_list)
                    
    
    
    while True:
        
        times_removed = 0
    
        for index, row in enumerate(copied_grid):

            count = 0
            prev_object = ' '
            
            for index2, objects in enumerate(row):
                current_object = copied_grid[(size - 1) - index][index2]

                if current_object == prev_object:
                    count += 1

                else:
                    count = 1
                    prev_object = current_object

                if count >= 3:

                    for index3 in range(index2 - count + 1, index2 + 1):

                        if copied_grid[(size - 1) - index][index3] != ' ':
                            points += 1
                            times_removed += 1
                            
                        copied_grid[(size - 1) - index][index3] = ' '

        for index, column in enumerate(copied_grid):

            count = 0
            prev_object = ' '
            
            for index2, row in enumerate(column):
                current_object = copied_grid[index2][index]

                if current_object == prev_object:
                    count += 1

                else:
                    count = 1
                    prev_object = current_object

                if count >= 3:

                    for index3 in range(index2 - count + 1, index2 + 1):

                        if copied_grid[index3][index] != ' ':
                            points += 1
                            times_removed += 1
                            
                        copied_grid[index3][index] = ' '

        if times_removed == 0:
            return 

        original_grid = list(copied_grid)
        printGrid()
        
        objectFill()
        printGrid()
        
        objectReplace()
        printGrid()
    
# Asks user if they want to play again

def replay():

    '''Prompts user if they would like to play again'''

    user_input = input('Replay? (y)es/(n)o ')

    while True:
        
        if user_input == 'y':
            return True

        elif user_input == 'n':
            return False

        else:
            print('Invalid input. (y) or (n) only.')
            continue

start_time = time.time()
printGrid()

while True:

    if points >= size * 10:
        end_time = time.time()
        win_time = end_time - start_time

        # win_time divided by 60 for time, minutes and seconds
        if win_time / 60 < 1:
            print(f"You've reached {points} points! Good job!\nTook {round(win_time)} seconds.")

            if replay():
                size = gridSize()
                original_grid = gridValues()
                copied_grid = list(original_grid)
                points = 0
                column_letters = list(string.ascii_uppercase[:size])
                row_numbers = list(range(size + 1))
                continue

            else:
                print('Quitting game...')
                raise SystemExit
            
        else:
            print(f"You've reached {points} points! Good job!\nTook {round(win_time / 60)} minutes.")

            if replay():
                points = 0
                continue

            else:
                print('Quitting game...')
                raise SystemExit

    else:
        objectCrush()
        print(f'\n{points} points.')
        objectSwap()
        printGrid()
        continue
    
