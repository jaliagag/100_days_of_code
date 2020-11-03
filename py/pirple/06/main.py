# Details:
     
#Create a function that takes in two parameters: rows, and columns, both of which are integers. The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. After drawing the board, your function should return True.


#Extra Credit:

#Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return False.

def tiktak(rows, columns): # 0, 1
    menosUno = rows-1
    for row in range(rows):
        if row % 2 == 0:
            for column in range(1,columns):
                if column % 2 == 1:
                    if column != menosUno:
                        print(" ", end="") # 0|1, 0|3
                    else:
                        print(" INTRO ") # 0|4
                else:
                    print("|", end="") # 0|0, 0|2
        else:
            print("-----") # 1
    return True

tiktak(10, 5)

# print('########')

#for row in range(5):
#    if row % 2 == 0:
     #   for column in range(1,6):
    #        if column % 2 == 1:
   #             if column != 5:
  #                  print(" ",end="")
 #               else:
#                    print(" ")
#            else:
#                print("|", end="")
#    else:
#        print("-----")
