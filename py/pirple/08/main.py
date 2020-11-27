# Homework Assignment #8: Input and Output (I/O)

#Details:
 
#Create a note-taking program. When a user starts it up, it should prompt them for a filename.

#If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.

#If they enter a file name that already exists, it should ask the user if they want:

#A) Read the file

#B) Delete the file and start over

#C) Append the file

#If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 

#Extra Credit:

#Allow the user to select a 4th option:

#D) Replace a single line

#If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:

#1) The line number they want to update.

#2) The text that should replace that line.

import os

thisPath = os.listdir()

def writeToTheFile(x):
    #print(x)
#def writeToTheFile(file2write):
    var = False
    while var == False:
        file2Modify = open(x, "w")
        aEscribir = input('what you want to write? ')
        if os.stat(x).st_size == 0:
            file2Modify.write(aEscribir)
            print('added!')
        if os.stat(x).st_size != 0:
            file2Modify.append(aEscribir)
            print('added!')


        again = input('wanna write something else? (y or n)')
        if again is "n":
            var = True
        elif again is "y":
            var = False
        else:
            print('wrong inpunt')
            again
            
        file2Modify.close()

        #tempPartData.append(aEscribir)
#        file2write.append(aEscribir)
#        again = input('wanna write something again? (y or n) ')
#        if again == y:
#            var = False
#        elif again == n:
#            var = True

def createFile ():
    var = False
    fileName = input('wharup yo! please input a name for your brand new file!: ')
    while var == False:
        if fileName in thisPath:
            print('name taken!')
            fileName = input('please, use another name for the file you want to create: ')
        else:
            print('file to be created!...')
            outputFile = open(fileName, "w")
            var = True
            writeToTheFile(fileName)
            outputFile.close()

createFile()

