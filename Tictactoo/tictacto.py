import numpy as np
import functions

board = np.zeros((3,3))

def print_board(board):
    for i in range (3):
        for j in range(3):
            print("|",board[i,j],"|", end=" ")
        print()

print("1 = User")
print("2 = Computer")

print(print_board(board))
for i in range(5):
    board = functions.user_input(board)
    board = functions.computer_choice(board)
    print(print_board(board))
    if(i > 1):
        if functions.user_wins(board):
            print("User wins as user got 3 in a straight line")
            break
        elif functions.computer_wins(board):
            print("Compute Wins as computer got 3 in a straight line first")
            break
        else:
            continue