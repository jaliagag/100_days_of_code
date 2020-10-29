# Python

Computer programming is the act of composing the selected programming language's elements in the order that will cause the desired effect.

There are two different ways of transforming a program from a high-level programming language into machine language:

1. compilation: the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing teh machine code; now you can distribute the file worldwide; the program that performs this translation is called a compiter or translator;
2. interpretation: you can translate the source program each time it has to be run; the progrma performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed; it also means that you cannot just distribute the source code as-is, because the end user needs the interpreter to execute it.

"""
def FunctionName(input):
    action
    return output

if it is indented, it's part of the function
"""

def addOne(Number):
    Number += 1
    return print(Number)

addOne(4)

# first calculated, then output added

addOne(2.1 + 3.8)