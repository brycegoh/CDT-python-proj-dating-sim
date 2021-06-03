'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game

Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''

import random
import util

def boardTemplatePrint():
    print("The board coordinate system looks like this:")
    print('   |   |')
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
    print('   |   |\n\n')
    return 

'''
boardPrint() was taken/modified from
https://www.codegrepper.com/code-examples/python/how+to+code+a+tic+tac+toe+game+with+ai+python
'''
def boardPrint(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    return 

'''
isWinner() was modified from
https://www.codegrepper.com/code-examples/python/how+to+code+a+tic+tac+toe+game+with+ai+python
'''
def isWinner(bo, le):
    winningRules = [
        (bo[6] == le and bo[7] == le and bo[8] == le),
        (bo[3] == le and bo[4] == le and bo[5] == le),
        (bo[0] == le and bo[1] == le and bo[2] == le),
        (bo[0] == le and bo[3] == le and bo[6] == le),
        (bo[1] == le and bo[4] == le and bo[7] == le),
        (bo[2] == le and bo[5] == le and bo[8] == le),
        (bo[0] == le and bo[4] == le and bo[8] == le),
        (bo[2] == le and bo[4] == le and bo[6] == le)
    ]
    return any( winningRules )


def randomComputerMove(board):
    possibleMoves = []
    for (index , value) in enumerate(board):
        if value == " ":
            possibleMoves.append(index)
    move = random.choice( possibleMoves )
    return move

def tictactoeStart(board):
    print('Welcome to Tic Tac Toe!')
    boardTemplatePrint()
    boardPrint(board)

    while (' ' in board):
        possibleMoves = []
        for (index , value) in enumerate(board):
            if value == " ":
                possibleMoves.append(index+1)
        move = 0
        while (move < 1 or move > 9) or move not in possibleMoves :
            print("Please input a valid integer")
            move = util.integerInput('Please select a position to place an \'X\' (1-9): ')
        board[move - 1] = 'X'
        boardPrint(board)
        
        if isWinner(board, 'X') :
            print("Congrats You Won!!")
            return True

        if ' ' in board:
            move = randomComputerMove(board)
            board[move] = 'O'
            print('Computer placed an \'O\' in position', move+1 , ':')
            boardPrint(board)
        
        if isWinner(board, 'O') :
            print("Computer wins!!")
            return False
    print("Its a tie...")
    return False