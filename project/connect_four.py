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

def create_board():
    """ create a new board and initialize all spaces to zero

        for now, this function creates a new board, initializes
        all places to zero and displays the board

    NICE TO HAVE:
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



def input_next_move(board, player_flag):
    """ input coordinates for next move based on user input

    """

    print "Select coordinates for next move, Player", player_flag, ":\n"
    row_coordinate = int(raw_input(" Which row? "))
    col_coordinate = int(raw_input(" Which col? "))

    if board[row_coordinate-1][col_coordinate-1] != 0:
        print "Coordinate is occupied! Try again!"
    else:
        board[row_coordinate - 1][col_coordinate - 1] = player_flag
        # switch player_flag only when valid move is made
        if player_flag == 1:
            player_flag += 1
        else:
            player_flag -= 1

    display_board(board)



    input_next_move(board, player_flag)


"""
    end of defining functions
    begin calling functions
"""

create_board()
display_board(board)
input_next_move(board, player_flag)
