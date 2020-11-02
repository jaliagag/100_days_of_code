# Details:
     
#Create a function that takes in two parameters: rows, and columns, both of which are integers. The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. After drawing the board, your function should return True.


#Extra Credit:

#Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return False.

#rows = 5


def tiktak(rows, columns):
    for row in range(rows):
        if row % 2 == 0:
            for column in range(1,columns):
                if column % 2 == 1:
                    if column != 5:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|")
        else:
            print("-----")
    return True

tiktak(5, 5)

