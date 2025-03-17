import random

objects = ['Q', 'R', 'S', 'T', 'U']

def gridValues():

  def rowValues():
    global objects
    random_object = random.choice(objects)
    row = [random_object]

    while len(row) != 8:
      random_object = random.choice(objects)
      row.append(random_object)

    return row

  grid = [rowValues()]

  while len(grid) != 8:
    grid.append(rowValues())

  return grid

points = 0
original_grid = gridValues()
column_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def printGrid():

  row_numbers = 8

  for row in original_grid:
    print(f'   +---+---+---+---+---+---+---+---+\n {row_numbers} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} |')
    row_numbers -= 1      

  print(f'   +---+---+---+---+---+---+---+---+\n     {column_letters[0]}   {column_letters[1]}   {column_letters[2]}   {column_letters[3]}   {column_letters[4]}   {column_letters[5]}   {column_letters[6]}   {column_letters[7]}')

  print("Points: ", points, "\n")
  if(points > 100):
    print("Congratuations! You got more than 100 points!")
    print("Bye.")
    raise SystemExit

def input_square():
  while True:
    user_input = input('Leter first, then number. (q) to quit\nPick a square: ')
    if user_input == 'q':
      print('Quitting...')
      raise SystemExit
    elif len(user_input) == 2:
      number = int(user_input[1])
      letter = user_input[0].capitalize()
      if (number < 1) or (number > 8):
        print('\nInvalid input. Acceptable numbers only.\n')
        continue
      if (letter < 'A') or (letter > 'H'):
        print('\nInvalid input. Acceptable letters only.\n')
        continue
      user_input = letter + str(number)
      break
  return user_input

def userInput():
  while True:
    first_square = input_square()
    second_square = input_square()
    if(first_square == second_square):
      print('\nInvalid input. Same slot.\n')
      continue
    if(first_square[1] != second_square[1]) and (first_square[0] != second_square[0]):
      print('\nInvalid input. Diagonal.\n')
      continue
    if(first_square[1] == second_square[1]) and (abs(ord(first_square[0]) - ord(second_square[0])) != 1):
      print('\nInvalid input. Too far.\n')
      continue
    if(first_square[0] == second_square[0]) and (abs(ord(first_square[1]) - ord(second_square[1])) != 1):
      print('\nInvalud input. Too far.\n')
      continue
    row1 = 8 - (ord(first_square[1]) - ord('0'))
    col1 = ord(first_square[0]) - ord('A')
    row2 = 8 - (ord(second_square[1]) - ord('0'))
    col2 = ord(second_square[0]) - ord('A')
    temp = original_grid[row1][col1]
    original_grid[row1][col1] = original_grid[row2][col2]
    original_grid[row2][col2] = temp
    break

def checkAndRemove():
  global original_grid
  global points

  while True:
    copied_grid = list(original_grid)
    total_removed = 0
    for row in range(8):
      last_letter = ' '
      count = 0
      for i in range(8):
        current_letter = original_grid[7 - row][i]
        if(current_letter == last_letter):
          count += 1
        else:
          count = 1
          last_letter = current_letter
        if(count >= 3):
          print("Replace {0}{1} to {2}{3} with space.".format(chr(ord('A') +(i - count + 1)), row + 1, chr(ord('A') + i), row + 1))
          for j in range(i - count + 1, i + 1):
            if(copied_grid[7 - row][j] != ' '):
              points += 1
              total_removed += 1
            copied_grid[7 - row][j] = ' '
 
    for col in range(8):
      last_letter = ' '
      count = 0
      for i in range(8):
        current_letter = original_grid[i][col]
        if(current_letter == last_letter):
          count += 1
        else:
          count = 1
          last_letter = current_letter
        if(count >= 3):
          print("Replace {0}{1} to {2}{3} with space.".format(chr(ord('A') + col), 8 - i, chr(ord('A') + col), 7 - i + count))
          for j in range(i - count + 1, i + 1):
            if(copied_grid[j][col] != ' '):
              points += 1
              total_removed += 1
            copied_grid[j][col] = ' '

    original_grid = list(copied_grid)
    printGrid()

    if(total_removed > 0):
      print("Let the letters drop.")
      while True:
        count = 0;
        for col in range(8):
          for row in range(8):
            if(original_grid[row][col] == ' '):
              if(row - 1 >= 0):
                if(original_grid[row - 1][col] != ' '):
                  original_grid[row][col] = original_grid[row - 1][col]
                  original_grid[row - 1][col] = ' '
                  count += 1
        if count == 0:
          break
                
    else:
      break
    
    printGrid()

    print("Generate random letters for empty squares.")
    for row in range(8):
      for col in range(8):
        if(original_grid[row][col] == ' '):
          original_grid[row][col] = random.choice(objects)

    printGrid()
    
print("Welcome to the game of LETTER BUSTER!\n")
print("Rules:")
print("A board of 8 by 8 squares is generated with random letters of 'Q', 'R', 'S', 'T' and 'U'.")
print("The player gets points when three or more of the same letters are adjacent in the same row or the same column.")
print("We will remove any cases where three or more of the same letters are adjacent in the same row or the same column.")
print("Then, the remaining letters rearrange by falling down to fill the gaps that just got removed.")
print("We will fill in gaps at the top with random new letters.")
print("On each turn, the player can choose to swap a piece with an adjacent piece.")
print("The game ends when the player scores over 100 points.\n")
print("Have fun!")
while True:
  printGrid()
  checkAndRemove()
  userInput()
  

