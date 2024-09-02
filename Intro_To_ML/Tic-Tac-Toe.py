# Alright!
# Let's create an X and O game using text based graphics.
# Using if else, then print for this would be suicidal, so let's try something different.
# I'll put everything in an array, 3 arrays rather.
# Let's go.

# These are the rows with the vertical X and O lines.
row_1 = ['    ', '|', '   ', '|', '   ']
row_2 = ['    ', '|', '   ', '|', '   ']
row_3 = ['    ', '|', '   ', '|', '   ']

# Let's get a board so we can use a row-column format to acces stuff.
board = [row_1, row_2, row_3]

# This is the Horizontal Line for the X and O format, to get it looking alright.
horizontal_line = ['____', '|', '___', '|', '___']

# This will be the sample display.
sample_row_1 = ['    ', '|', '   ', '|', '   ']
sample_row_2 = ['    ', '|', '   ', '|', '   ']
sample_row_3 = ['    ', '|', '   ', '|', '   ']
# We will print out the sample display once the game starts.

def sample():
  # Let's print a welcome message.
    print('Welcome to the X and O game!')
    print('Here is a sample of the board:')

    print(''.join(sample_row_1))
    print(''.join(horizontal_line))
    print(''.join(sample_row_2))
    print(''.join(horizontal_line))
    print(''.join(sample_row_3))

    print(f'''The Board uses a r,c input tactic. \n
          What I mean by this is that if you wanted to play an x at row 1, column 1, you would input 1,1 and the board would become: ''')

    # Input X in the firct column of row 1
    sample_row_1[0] = '  X ' # Hmm, the space need to keep semantics vary. That may be a problem.
                             # The exact semantics look like 3 spaces for values that fall in array index 0 or game column 1
                             # 2 spaces for values that fall in array index 2 or game column 2
                             # and 2 spacec for values that fall in array index 4 or game column 3
                             # I'll create a "spaces" dict with the requirements.

    print(f'''
          {''.join(sample_row_1)}
          {''.join(horizontal_line)}
          {''.join(sample_row_2)}
          {''.join(horizontal_line)}
          {''.join(sample_row_3)}
      ''')

    print('And if player 2 wants to add an O to row 2, column 3 they would input 2,3 and the board would become:')

    # Input O in the third column of row 2
    sample_row_2[2] = ' O '

    print(f'''
          {''.join(sample_row_1)}
          {''.join(horizontal_line)}
          {''.join(sample_row_2)}
          {''.join(horizontal_line)}
          {''.join(sample_row_3)}
      ''')


# Note that valid array columns for each row are columns : 0, 2, 4. This should be noted for array indexing purposes.

# let's create the moves dict.
moves = {
    '1,1' : 0,
    '1,2' : 2,
    '1,3' : 4,
    '2,1' : 0,
    '2,2' : 2,
    '2,3' : 4,
    '3,1' : 0,
    '3,2' : 2,
    '3,3' : 4,
}

# Let's create the spaces dict for each player to keep semantics.
player_1_spaces = {
    0 : '  X ',
    2 : ' X ',
    4 : ' X ',
}

player_2_spaces = {
    0 : '  O ',
    2 : ' O ',
    4 : ' O ',
}


# Let's create a game play function.
def game_play():


    # Let's create an update board function:
    def update_board(row, column, player):
      # get move
      move = moves[f'{row},{column}']
      # Update board with move for this player
      if player == 1:
        # Note that i did row - 1 due to the zero based indexing.
        board[row-1][move] = player_1_spaces[move]
      else:
        board[row-1][move] = player_2_spaces[move]
      # Print the board
      print(''.join(board[0]))
      print(''.join(horizontal_line))
      print(''.join(board[1]))
      print(''.join(horizontal_line))
      print(''.join(board[2]))


    # Let's create an array for storing occupied columns.
    occupied_columns = []

    # Let's create a variable to keep track of the number of moves till the game ends.
    # Note that X and O involves at most 9 moves
    move_count = 9

    # Let's create a check win function.


    def check_win():
        # This function checks for a win.
        # Horizontal, vertical, and diagonal checks
        winning_combinations = [
            [board[0][0], board[0][2], board[0][4]],  # Row 1
            [board[1][0], board[1][2], board[1][4]],  # Row 2
            [board[2][0], board[2][2], board[2][4]],  # Row 3
            [board[0][0], board[1][0], board[2][0]],  # Column 1
            [board[0][2], board[1][2], board[2][2]],  # Column 2
            [board[0][4], board[1][4], board[2][4]],  # Column 3
            [board[0][0], board[1][2], board[2][4]],  # Diagonal 1
            [board[0][4], board[1][2], board[2][0]]   # Diagonal 2
        ]
        # This isn't pretty, but it works.
        for combination in winning_combinations:
            if 'X'in combination[0] and 'X'in combination[1] and 'X'in combination[2]:
                return True
            elif 'O'in combination[0] and 'O'in combination[1] and 'O'in combination[2]:
                return True
        return False


    # Let's play the game.
    while move_count > 0:
      for player in [1, 2]:
        # Let's get the user input.
        user_input = input(f'Player {player}, please enter your move in the form r,c (Note that you are {"X" if player == 1 else "O"}): ').strip()
        # Let's check if the input is valid.
        if user_input in moves:
          # Let's check if the column is occupied.
                  tuple_input = tuple(user_input.split(','))
                  row = int(tuple_input[0])
                  column = int(tuple_input[1])
        else:
          print('Not a valid input! Player 2 plays now.')
          continue

        # Let's check if the column is occupied.
        if f'{row},{column}' in occupied_columns:
          # if it is, print a message and continue.
          print('\n Nah fam, can\'t you see there\'s something there? Next Player!')
          # This continue statement should now go back to the top of the for loop and move to 1 if it was in 2, and vice vera.
          continue
        else:
          # if it isn't, add it to the occupied columns list and update the board.
          occupied_columns.append(f'{row},{column}')
          update_board(row, column, player)
          # Let's update the move count.
          move_count -= 1
          # Let's check if the game is over.
          if check_win():
            print(f'Player {player} wins!')
            return
    # If move count exhausted, announce the game as a draw and end it.
    if move_count == 0:
      return 'It\'s a draw!'




# I'll use a main function for this game
def main():
    # Print the sample display.
    sample()
    # Start the game.
    game_play()

# Run the main function.
main()
