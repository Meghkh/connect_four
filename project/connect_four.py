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

        decided to separate the displaying of the board from the creating
        of a new board so that it will be easier to later implement a new
        game function.
    """

    print "\n"
    for row in board:
#        print " ".join(str(row))
        print "\t\t\t" + str(row)
    print "\n"

#def input_next_move(board):
    """ input coordinates for next move based on user input

    """



"""
    end of defining functions
    begin calling functions
"""

create_board()
display_board(board)
