# Details:
     
#Create a function that takes in two parameters: rows, and columns, both of which are integers. The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. After drawing the board, your function should return True.


#Extra Credit:

#Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return False.

import os

def tiktak(rows, columns):
    Trows, Tcolumns = os.popen('stty size', 'r').read().split()
    if rows > int(Trows) or columns > int(Tcolumns):
        return False
    else:
        dash = '-'
        rows *= 2
        columns *= 2
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
                print(dash*columns)
        return True

tiktak(5, 5)
