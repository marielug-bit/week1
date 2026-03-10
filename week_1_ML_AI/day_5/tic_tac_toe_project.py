# ==================================================
# 🎮 Tic Tac Toe - Instructions
# ==================================================
# Tic Tac Toe is played on a 3x3 grid.
# Players take turns marking empty squares with their symbol ('O' or 'X').
# The first player to get three of their symbols in a row
# (horizontally, vertically, or diagonally) wins.
# If all squares are filled and no player has three in a row, the game is a tie.

# ==================================================
# Step 1: Representing the Game Board
# ==================================================
# - You need a way to represent the 3x3 grid.
# - A list of lists (a 2D list) is a good choice.
# - Initially, each cell should be empty (example: a space ' ').
#
# Example board structure: 
board = [
   [' ', ' ', ' '],
   [' ', ' ', ' '],
   [' ', ' ', ' ']
 ]

# ==================================================
# Step 2: Displaying the Game Board
# ==================================================
# Create a function: display_board(board)
# - Prints the current state of the board
# - Should visually represent the 3x3 grid
# - Format it so it’s easy to read (lines + separators)
#
# Example display:
#  X | O |  
# ---+---+---
#    | X |  
# ---+---+---
#  O |   | X

def display_board(board):
    print('-----------')
    print(' '+ ' | '.join(board[0]))
    print('---+---+---')
    print(' '+ ' | '.join(board[1]))
    print('---+---+---')
    print(' '+ ' | '.join(board[2]))
    print('-----------')


# ==================================================
# Step 3: Getting Player Input
# ==================================================
# Create a function: player_input(board, player)
# - Asks the player for their move (row and column)
# - Validates input:
#   1) row and col are in range (0-2 or 1-3 depending on your choice)
#   2) chosen cell is empty
# - Returns (row, col) or directly updates the board (your choice)
#
# Tip: keep asking until the input is valid.
def player_input(board, player):
    print(f'Player {player}, it is your turn.')
    move_raw = input('Enter row: ')
    move_col = input('Enter column: ')
    val = 1
    
    if not (move_raw.isdigit() and move_col.isdigit()):
        val = 0
    elif not (0 <= int(move_raw) <= 2 and 0 <= int(move_col) <= 2):
        val = 0 
    elif board[int(move_raw)][int(move_col)] != ' ':
        val = 0

    while not val:
        print('Invalid input')
        move_raw = input('Enter row: ')
        move_col = input('Enter column: ')
        if move_raw.isdigit() and move_col.isdigit() and 0 <= int(move_raw) <= 2 and 0 <= int(move_col) <= 2:
            if board[int(move_raw)][int(move_col)] == ' ':
                val = 1
    
    return (int(move_raw),int(move_col))

def change_the_board(tup,symbol):
    a,b = tup
    board[a][b] = symbol
  
    
# ==================================================
# Step 4: Checking for a Winner
# ==================================================
# Create a function: check_win(board, player)
# - Checks all winning combinations:
#   * 3 rows
#   * 3 columns
#   * 2 diagonals
# - If player has 3 in a row -> return True
# - Otherwise -> return False

def board_col(board):
    lst_col = []
    for i in range(len(board[0])):
        ls = [raw[i] for raw in board]
        lst_col.append(ls)
    return lst_col  

def check_win(board, player):
    for raw in board:
        if ''.join(raw) == player*3:
            return True
    for col in board_col(board):
        if ''.join(col)== player*3:
            return True
    if board[0][0] == board [1][1] == board[2][2] == player:
        return True
    if board[0][2] == board [1][1] == board[2][0] == player:
        return True
    return False


  
        
# ==================================================
# Step 5: Checking for a Tie
# ==================================================
# Create a function: check_tie(board)
# - Returns True if:
#   * all cells are full
#   * AND there is no winner
# - Otherwise returns False

def check_tie(board):
    for raw in board:
        for char in raw:
            if char == ' ':
                return False
    return True

def change_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'
# ==================================================
# Step 6: The Main Game Loop
# ==================================================
# Create a function: play()
# - Initialize the board
# - Set the first player ('X' or 'O')
# - Use a while loop that runs until:
#   * someone wins OR
#   * there is a tie
def play():
    players = ['X','O']
    current_player = players[0]

    while True:
        display_board(board)
        tup = player_input(board, current_player)
        change_the_board(tup,current_player)
        if check_win(board,current_player):
            print(f'player {current_player} wins')
            display_board(board)
            break
        elif check_tie(board):
            print('There is a tie')
            display_board(board)
            break
        current_player = change_player(current_player)

play()
    

# Inside the loop:
# 1) display_board(board)
# 2) get player move (row, col) using player_input(...)
# 3) update board with player's symbol
# 4) check_win(board, player)
# 5) check_tie(board)
# 6) switch player (X <-> O)
#
# After loop:
# - display the final board
# - print the result: winner or tie

# ==================================================
# Tips / Good Practice
# ==================================================
# - Create helper functions to keep code clean.
# - Single responsibility principle:
#   each function should do ONE thing well.
# - Switching players:
#   player = 'O' if player == 'X' else 'X'
# - Store symbols as strings: 'X' and 'O'