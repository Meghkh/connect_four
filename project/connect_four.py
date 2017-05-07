"""
Connect Four game

about/instructions
"""

#print "Hello, World!"

""" initialize board object with rows and columns
    could later be replaced with a function that intakes
    user defined board size
"""

board = []
cols = 7
rows = 6

player_flag = 1
win_flag = 0

def create_board():
    """ create a new board and initialize all spaces to zero

        for now, this function creates a new board, initializes
        all places to zero and displays the board

        by returning the board and using as parameters for other
        board sizes, other functions should be able to handle
        changing board sizes
    """

    for i in range(rows):
        board.append([])
        for j in range(cols):
            board[i].append(0)

    return board



def display_board(board):
    """ display the board
        include row and column identifiers to help users select move

        separate the displaying of the board from the creating
        of a new board so that board can be viewed without
        re-initializing
    """

    print "\n"
    print "\tROWS\n\t\tCOLUMNS"
#    print "\t\t\tCOLUMNS"
    for row in board:
#        print " ".join(str(row))
        print "\t\t", "", "\t", str(row)
    print "\n"



def input_next_move(board, player_flag, win_flag):
    """ input coordinates for next move based on user input

        NEED TO ADD
            - user input sanitation to keep indexing of array within range

    """

    print "Select coordinates for next move, Player", player_flag, ":\n"
#    while row_coordinate != range()
    row_coordinate = int(raw_input(" Which row? "))


    col_coordinate = int(raw_input(" Which col? "))

    if board[row_coordinate - 1][col_coordinate - 1] != 0:
        print "Coordinate is occupied! Try again!"
    else:
        board[row_coordinate - 1][col_coordinate - 1] = player_flag
        # switch player_flag only when valid move is made
        if player_flag == 1:
            player_flag += 1
        else:
            player_flag -= 1

    display_board(board)
    check_win_conditions(board, win_flag)
    input_next_move(board, player_flag, win_flag)



def check_win_conditions(board, win_flag):
    """ checks for a win condition by either user

    """

    board_height = len(board)
    board_width = len(board[0])

    for i in range(board_height):
        for j in range(board_width - 3):

            # checks for horizontal win condition
            if board[i][j] == 1 and board[i][j+1] == 1 and board[i][j+2] == 1 and board[i][j+3] == 1:
                win_flag = 1
            elif board[i][j] == 2 and board[i][j+1] == 2 and board[i][j+2] == 2 and board[i][j+3] == 2:
                win_flag = 2

            # checks for vertical win condition
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1:
                win_flag = 1
            elif board[i][j] == 2 and board[i+1][j] == 2 and board[i+2][j] == 2 and board[i+3][j] == 2:
                win_flag = 2



            # check for diagonal win condition UL to LR

            # checks for diagonal win condition LL to UP


    if win_flag != 0:
        print "Congrats, Player", str(win_flag), "you won!"

"""
    end of defining functions
    begin calling functions
"""

create_board()
display_board(board)
#check_win_conditions(board, win_flag)
input_next_move(board, player_flag, win_flag)


#while check_win_conditions(board, win_flag) == 0:
#    input_next_move(board, player_flag, win_flag)
