import time

# Setup for making the game run

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

playing = True

# Code for what the user sees starts here.

print("Welcome to the Python 3 Tic-Tac-Toe game! This will be an incredibly simple game you can play on the console.")
time.sleep(2)
print("First, to start things off, can you tell me your name?")
name = input()
print("Nice! I love your name, " + name + ". Glad to have you with us.")
time.sleep(1)
print("Bringing up the game menu now...")
time.sleep(2)

while playing:
    print("To go straight into the game, type PLAY. If you would like a tutorial, type TUTORIAL."
          " If you wish to exit, type EXIT.")
    player_decision = input()

    if player_decision == "TUTORIAL":
        print("Great! Here's how the game works, " + name + ".")
    elif player_decision == "EXIT":
        print("Thanks for playing, " + name + "! Hope to see you again soon.")
        playing = False
    #
    # turn = "X"
    #
    # for i in range(9):
    #     print_board(the_board)
    #     print("Now it's " + turn + "'s turn. Place the " + turn + " onto which space?")
    #     move = input()
    #     the_board[move] = turn
    #     if turn == "X":
    #         turn = "O"
    #     else:
    #         turn = "X"

# print_board(the_board)
