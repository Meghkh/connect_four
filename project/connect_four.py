"""
Connect Four game

about/instructions
"""

#print "Hello, World!"
board = []
cols = 7
rows = 6

def create_board():
    # create a new board and initialize all spaces to zero

    for i in range(cols):
        for j in range(rows):
            board.append(0)

    return board



#    print board

def display_board(board):
    # display the board

#    print "\n"
#    print "\n".join(str(board[:]))
#    print "\n"

#    print str(board)

    for row in board:
#        print " ".join(str(board[i]))
        if row % cols == 0:
            print '\n'
        print board[row]
#    print('\n'.join([''.join(['{:}'.format(item) for str(item) in row])
#      for row in board]))


create_board()
display_board(board)
