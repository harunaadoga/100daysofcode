import pprint
#a tic tac toe game
board = {'top-Left': '', 'top-Middle': '', 'top-Right': '',
        'mid-Left': ' ', 'mid-Middle': ' ', 'mid-Right': ' ',
        'low-Left': ' ', 'low-Middle': '', 'low-Right': ' '}

#print the board
def printBoard(board):
    print(board['top-Left'] + '|' + board['top-Middle'] + '|' + board['top-Right'])
    print('-+-+-')
    print(board['mid-Left'] + '|' + board['mid-Middle'] + '|' + board['mid-Right'])
    print('-+-+-')
    print(board['low-Left'] + '|' + board['low-Middle'] + '|' + board['low-Right'])
#manipulate turns
turn = 'X'
for i in range(9):
    printBoard(board)
    print('Turn for '+ turn+ '. Move on which space?')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printBoard(board)