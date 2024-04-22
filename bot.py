from random import randint
from os import system, name

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
    print('   |   |\n')

def available(board,num):
    if num>9:
        return False
    return False if num==0 else playboard[num]==' '

def win(board,ch):

    if ( board[1:4]==[ch,ch,ch] ) or ( board[4:7]==[ch,ch,ch] ) or ( board[7:]==[ch,ch,ch] ) : # checks rows
        return True
    if ( board[1::3]==[ch,ch,ch] ) or ( board[2::3]==[ch,ch,ch] ) or ( board[3::3]==[ch,ch,ch] ) : # check columns
        return True
    if ( board[1::4]==[ch,ch,ch] ) or ( board[3:9:2]==[ch,ch,ch] ) : # checks diagonals
        return True
    return False

def play():
    player1 = input("Enter your character : ")
    player2 = input("Enter your character 2: ")
    playboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while ' ' in playboard[1:]:
        # clear output screen
        system('cls') if name == 'nt' else system('clear')

        # prints title
        title()

        # displays the board
        display(playboard)

        a = 0
        b = 0

        # place moves
        while (a not in range(1,10)) and (not available(playboard, a)):
            a = int(input("Player 1 : "))
        playboard[a]=player1

        if win(playboard, player1):
            winflag = "player1"
            break

        while (b not in range(1,10)) and (not available(playboard, b)):
            b = int(input("Player 2 : "))
        playboard[b]=player2

        if win(playboard, player2):
            winflag = "player2"
            break
    
    system('cls') if name == 'nt' else system('clear')
    title()
    display(playboard)

    print(f"Player {1 if winflag=='player1' else 2} wins the game !!! \n\n")

playmore = 'y'
while playmore=='y':
    
    play()

    playmore = input("Do you want to play more? ")