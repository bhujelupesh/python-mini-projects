import numpy as np
import random 

def user_input(board):
    print("Player 1")
    row = int(input("Enter the row value (0-2): "))
    column = int(input("Enter the column value (0-2): "))
    check_value = board[row,column]
    if check_value != 'x'or check_value != 'o':
        value = 'x'
        board[row,column] = value
    else:
        print("Already filled")
        user_input(board)
    return board

def user_input2(board):
    print("Player 2")
    row = int(input("Enter the row value (0-2): "))
    column = int(input("Enter the column value (0-2): "))
    check_value = board[row,column]
    if check_value != 'x' or check_value != 'o':
        board[row,column] = 'o'
    else:
        print("Already filled")
        user_input(board)
    return board

def computer_choice(board):
    row = random.randint(0,2)
    column = random.randint(0,2)
    if board[row,column] != 'x' or board[row,column] != 'o':
        board[row,column] = 'o'
    else:
        computer_choice(board)
    return board

def computer_wins(board):
    if board[0,0] == board[0,1] == board[0,2] == 'o':
        return True

    elif board[1,0] == board[1,1] == board[1,2] == 'o':
        return True  
      
    elif board[2,0] == board[2,1] == board[2,2] == 'o':
        return True

    elif board[0,0] == board[1,0] == board[2,0] == 'o':
        return True

    elif board[0,1] == board[1,1] == board[2,1] == 'o':
        return True

    elif board[0,2] == board[1,2] == board[2,2] == 'o':
        return True
    
    elif board[0,0] == board[1,1] == board[2,2] == 'o':
        return True

    elif board[0,2] == board[1,1] == board[2,0] == 'o':
        return True

    else:
        return False

def user_wins(board):
    if board[0,0] == board[0,1] == board[0,2] == 'x':
        return True

    elif board[1,0] == board[1,1] == board[1,2] == 'x':
        return True
    
    elif board[2,0] == board[2,1] == board[2,2] == 'x':
        return True

    elif board[0,0] == board[1,0] == board[2,0] == 'x':
        return True

    elif board[0,1] == board[1,1] == board[2,1] == 'x':
        return True

    elif board[0,2] == board[1,2] == board[2,2] == 'x':
        return True
    
    elif board[0,0] == board[1,1] == board[2,2] == 'x':
        return True

    elif board[0,2] == board[1,1] == board[2,0] == 'x':
        return True

    else:
        return False
    
def win_checker(board):
        if user_wins(board):
            print("Player1 wins as Player1 got 3 in a straight line")
            return 1
        elif computer_wins(board):
            print("Player2 Wins as Player2 got 3 in a straight line first")
            return 1
        else: 
            return 
