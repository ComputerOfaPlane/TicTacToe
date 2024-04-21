from random import randint
from os import system, name

playboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = {'char':None}

def title():
    print("___________.__               ___________                     ___________            ")
    print("\__    ___/|__| ____         \__    ___/____    ____         \__    ___/___   ____  ")
    print("  |    |   |  |/ ___\   ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ ")
    print("  |    |   |  \  \___  /_____/ |    |   / __ \\\\  \___  /_____/ |    |(  <_> )  ___/ ")
    print("  |____|   |__|\___  >         |____|  (____  /\___  >         |____| \____/ \___  >")
    print("                   \/                       \/     \/                            \/ ")

def display(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')



def win(board,ch):

    if ( board[1:4]==[ch,ch,ch] ) or ( board[4:7]==[ch,ch,ch] ) or ( board[7:]==[ch,ch,ch] ) : # checks rows
        return True
    if ( board[1::3]==[ch,ch,ch] ) or ( board[2::3]==[ch,ch,ch] ) or ( board[3::3]==[ch,ch,ch] ) : # check columns
        return True
    if ( board[1::4]==[ch,ch,ch] ) or ( board[3:9:2]==[ch,ch,ch] ) : # checks diagonals
        return True
    return False

test_WIN =   [[' ','X','X','X',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ','X','X','X',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ','X','X','X'],
              [' ','X',' ',' ','X',' ',' ','X',' ',' '],
              [' ',' ','X',' ',' ','X',' ',' ','X',' '],
              [' ',' ',' ','X',' ',' ','X',' ',' ','X'],
              [' ','X',' ',' ',' ','X',' ',' ',' ','X'],
              [' ',' ',' ','X',' ','X',' ','X',' ',' ']]
test_lose = [' ',' ','X',' ','X',' ','X',' ','X',' ']
test_board = [' ','X','O','X','O','X','O','X','O','X']



def play():

    # clear output screen
    system('cls') if name == 'nt' else system('clear')

    # prints title
    title()

    # displays the board
    display(test_board)

    # player


play()