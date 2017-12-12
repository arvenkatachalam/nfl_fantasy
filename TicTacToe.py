import random as rd

def display_board(board):
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')

def player_input():
    marker = ''
    goodanswer = False
    while goodanswer == False:
        marker = input('Player 1: Do you want to be X or O?').upper()
        if marker == 'O':
            goodanswer = True
            return ['O','X']
        if marker == 'X':
            goodanswer = True
            return ['X','O']
        else:
            print('Try again, dumbass!')

def place_marker(board, marker, position):
        board[position] = marker
        return board

def win_check(board,mark):
    return ((board(7) == board(8) == board(9) == mark) or
    (board(4) == board(5) == board(6) == mark) or
    (board(1) == board(2) == board(3) == mark) or
    (board(7) == board(4) == board(1) == mark) or
    (board(8) == board(5) == board(2) == mark) or
    (board(9) == board(6) == board(3) == mark) or
    (board(1) == board(5) == board(9) == mark) or
    (board(7) == board(5) == board(4) == mark))

def choose_first():
    rand = 0
    rand = rd.randint(0,1)
    if(rand == 0):
        print('Player 1 goes first')
    elif(rand == 1):
        print('Player 2 goes first')

def space_check(board, position):
    if (board[position] == 'X' or board[position] == 'O'):
        return True
    else:
        return False

def full_board_check(board):
    for spot in board:
        if (board[spot] == 'X' or board[spot] == 'O'):
            return True
            break
    return False

def main():
    print('Welcome to Tic Tac Toe!')


if __name__ == "__main__": main()
