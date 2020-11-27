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
import sys

thisPath = os.listdir()

def fileExists(x):
    qUno = int(input('wait up... file already exists! - would you like to \n(1) add to existing file, \n(2) read the file, \n(3) create a new file, \n(4) replace a single line, \n(5) cancel the operation, \n(6) or delete the file? \n(please, input either 1, 2, 3, 4, 5 or 6) '))
    if qUno == 1:
        add2File(x)
    if qUno == 2:
        f = open(x, "r")
        print(f.read())
        f.close()
        exit()
    if qUno == 3:
        write2File(x)
    if qUno == 4:
        replaceLine(x)
    if qUno == 5:
        exit()
        print('bye!')
    if qUno == 6:
        os.remove(x)
        print('file deleted!')
    return

def replaceLine(which):
    f = open(which, "r")
    listLines = f.readlines()
    lineNum = int(input('which line would you like to replace? '))
    lineNum -= 1
    whatReplace = input('with what do you want to replace that filthy line? ')
    f = open(which, "w")
    listLines[lineNum] = whatReplace + "\n"
    f.writelines(listLines)
    f.close()

    print('replaced!')
    exit()

def add2File(which):
    file = open(which, "a")
    what = input("what do you want to add? ")
    file.write(what)
    file.write("\n")
    file.close()
    print('added!')
    exit()
    return

def write2File(which):
    file = open(which, "w")
    what = input("what do you want to add? ")
    file.write(what)
    file.write("\n")
    file.close()
    print('written!')
    exit()
    return

def fileNotExists(x):
    file = open(x, "w")
    qDos = input('what do you want to write to this magnificent new file? ')
    file.write(qDos)
    file.write("\n")
    file.close()
    return

def notas():
    var = False
    fileName = input('welcome! please input a name for your brand new file!: ')
    while var == False:
        if fileName in thisPath:
            fileExists(fileName)
            var = True 
        else:
            fileNotExists(fileName)
            var = True
    return
notas()

