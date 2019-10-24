# game board
board = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]

# current player is a STRING containing 'X'
current_player = 'X'

# winner is always FALSE (until it's not)
winner = False

filled_spaces = 0
endgame = False
valid_move = True

# Print the board when game starts
print("\nThis is a Human(X) vs Computer(O) TicTacToe game.")

def game_over():
    global endgame
    if current_player == 'X':
        print("The winner is Player X. Game over.")
        endgame = True
        
    elif current_player == 'O':
        print("The winner is Player O. Game over.")
        endgame = True    

def check_win():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == board[0][2] and not board[0][0] == '_':
        game_over()


    elif board[1][0] == board[1][1]  and  board[1][1] == board[1][2]  and  board[1][0] == board[1][2]  and not board[1][0] == '_':
        game_over()


    elif  board[2][0] == board[2][1]  and  board[2][1] == board[2][2]  and  board[2][0] == board[2][2] and not board[2][0] == '_':
        game_over()

    
    elif board[0][0] == board[1][0]  and  board[1][0] == board[2][0]  and  board[0][0] == board[2][0]  and not board[0][0] == '_':
        game_over()


    elif  board[0][1] == board[1][1]  and board[1][1] == board[2][1] and  board[0][1] == board[2][1]  and not board[0][1] == '_':
        game_over()
 

    elif board[0][2] == board[1][2] and  board[1][2] == board[2][2]  and  board[0][2] == board[2][2]  and not board[0][2] == '_':
        game_over()


    elif  board[0][0] == board[1][1]  and board[1][1] == board[2][2]  and  board[0][0] == board[2][2]  and not board[0][0] == '_':
        game_over()

    elif  board[0][2] == board[1][1] and  board[1][1] == board[2][0]  and  board[0][2] == board[2][0]  and not board[0][2] == '_':
        game_over()

def summon_board():
    for rows in board:
        print(rows)

summon_board()

xxx = 0
yyy = 0
def computer_randomize_coordinates():
    print("randomizing")
    global xxx
    global yyy
    from random import randrange
    xxx= randrange(3)
    yyy = randrange(3)

def computer_actions():
    global filled_spaces
    global current_player
    # Computer's turn
    
    # Computer to summon coordinates
    computer_randomize_coordinates()

    # Computer checks if position is taken, otherwise, finds another position. Ad infinitum
    while not(board[xxx][yyy] == '_') and filled_spaces < 9:
        computer_randomize_coordinates()
        

    # computer inputs into board
    board[xxx][yyy] = 'O'
    print("\nThe board has now been updated. It is now the human's turn again.")
    current_player = 'X'
    filled_spaces += 1
    check_win()
    summon_board()



while ( filled_spaces < 9) and (endgame == False):
    while True:
        row_number = input("")
        # Permissible row numbers: 1, 2 and 3 only.
        if ( (row_number == "1") or (row_number == "2") or (row_number == "3")):
            break
        else:
            print("The only possible input for the row numbers are 1, 2 and 3. Try again.")

    while True:
        column_number = input("")
        # Permissible column numbers: 1, 2 and 3 only.
        if ( (column_number == "1") or (column_number == "2") or (column_number == "3")):
            break
        else:
            print("The only possible input for the column numbers are 1, 2 and 3. Try again.")
    
    # check if it's a valid move
    if not(board[int(row_number) - 1][int(column_number) - 1] == '_'):
        print("This is an invalid move.\nSomeone has already filled in the position.\nPlease resubmit your coordinates.")
        valid_move = False
    else: 
        valid_move = True

    # updates and prints the board, then change the players' turn
    if current_player == 'X' and valid_move == True:
        board[int(row_number) - 1][int(column_number) - 1] = 'X'
        current_player = 'O'
        filled_spaces += 1
        print("You have placed a cell.")
        summon_board()
        check_win()

    # Computer's turn
    if filled_spaces < 9 and valid_move == True:
        computer_actions()
    
    if endgame == True:
        break
    else:
        print()


"""
git clone git@github.com:nahiphog/challenge-fswd-python-tic-tac-toe-vs-computer.git
"""