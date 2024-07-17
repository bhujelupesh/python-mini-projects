import numpy as np
import functions

board_structure = np.zeros((3,3))
board_structure = board_structure.astype(int)
board = board_structure.astype(str)

def print_board(board):
    for i in range (3):
        for j in range(3):
            print("|",board[i,j],"|", end=" ")
        print()

print("---------------------Tic Tac Too------------------------")
print("Welcome to the game......")
print("Select Mode:")
print("1. Single Player...")
print("2. Two Player...")
choice = int(input("Enter your choice : "))

if choice == 1:
    print("x = User")
    print("o = Computer")

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

elif choice == 2:
    print("1 = Player 1")
    print("2 = Player 2")
    
    print(print_board(board))
    for i in range(5):
        board = functions.user_input(board)
        print_board(board)
        x = functions.win_checker(board)
        if x == 1:
            break
        board = functions.user_input2(board)
        print(print_board(board))
        x = functions.win_checker(board)
        if x == 1:
            break
