# Project #1: A Simple Game

#Details:
 
#Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, your task is create a Connect 4 game in Python. Before you get started, please watch this video on the rules of Connect 4:

#https://youtu.be/utXzIFEVPjA

# Rules
# 2 players 6 rows, 7 columns
# goal is to get 4 pieces in a row, diagonal, vertical, horizontal

#Once you've got the rules down, your assignment should be fairly straightforward. You'll want to draw the board, and allow two players to take turns placing their pieces on the board (but as you learned above, they can only do so by choosing a column, not a row). The first player to get 4 across or diagonal should win!

#Normally the pieces would be red and black, but you can use X and O instead.

#Extra Credit:

#Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a package like termcolor into your project. We're going to cover importing later in the course, but try and see if you can figure it out on your own. Or you might be able to find unicode characters to use instead, depending on what your system supports. Here's a hint: print(u'\u2B24')

import os

def board (rows, columns):
    Trows, Tcolumns = os.popen('stty size', 'r').read().split()
    if rows > int(Trows) or columns > int(Tcolumns):
        return False
    else:
        dash = '-'
        rows *= 2
        columns *= 2
        dashes = dash*(columns+1)
        menosUno = columns-1
        for row in range(rows):
            if row % 2 == 0:
                for column in range(1,columns):
                    if column % 2 == 1:
                        if column == menosUno:
                            print(" |")
                        else:
                            print(" ", end="")
                    else:
                        print("|", end="")
            else:
                print(dashes)
        return True

board(6, 7)

campo = []

turn = 0
score = 0
counter = 0

def changeTurn():
    global turn
    if turn == 1:
        turn = 0
    elif turn == 0:
        turn = 1

def wrong(param):
    if param <= 0 or param > 7:
        print('wrong column number - please, input a valid column number, 1 through 7')
        changeTurn()

while counter < 10:
    counter += 1
    if turn == 0:
        play = int(input('player 1: select a column 1 - 7 to make your move: '))
        wrong(play)
    if turn == 1:
        play = int(input('player 2: select a column 1 - 7 to make your move: '))
        wrong(play)
    changeTurn()

    print(counter)




