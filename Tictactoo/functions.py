import numpy as np
import random 

def user_input(board):
    row = int(input("Enter the row value (0-2): "))
    column = int(input("Enter the column value (0-2): "))
    check_value = board[row,column]
    if check_value == 0:
        board[row,column] = 1
    else:
        print("Already filled")
        user_input(board)
    return board

def computer_choice(board):
    row = random.randint(0,2)
    column = random.randint(0,2)
    if board[row,column] == 0:
        board[row,column] = 2
    else:
        computer_choice(board)
    return board

def computer_wins(board):
    if board[0,0] == board[0,1] == board[0,2] == 2:
        return True

    elif board[1,0] == board[1,1] == board[1,2] == 2:
        return True  
      
    elif board[2,0] == board[2,1] == board[2,2] == 2:
        return True

    elif board[0,0] == board[1,0] == board[2,0] == 2:
        return True

    elif board[0,1] == board[1,1] == board[2,1] == 2:
        return True

    elif board[0,2] == board[1,2] == board[2,2] == 2:
        return True
    
    elif board[0,0] == board[1,1] == board[2,2] == 2:
        return True

    elif board[0,2] == board[1,1] == board[2,0] == 2:
        return True

    else:
        return False

def user_wins(board):
    if board[0,0] == board[0,1] == board[0,2] == 1:
        return True

    elif board[1,0] == board[1,1] == board[1,2] == 1:
        return True
    
    elif board[2,0] == board[2,1] == board[2,2] == 1:
        return True

    elif board[0,0] == board[1,0] == board[2,0] == 1:
        return True

    elif board[0,1] == board[1,1] == board[2,1] == 1:
        return True

    elif board[0,2] == board[1,2] == board[2,2] == 1:
        return True
    
    elif board[0,0] == board[1,1] == board[2,2] == 1:
        return True

    elif board[0,2] == board[1,1] == board[2,0] == 1:
        return True

    else:
        return False