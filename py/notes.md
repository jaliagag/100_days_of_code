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

## first calculated, then output added

addOne(2.1 + 3.8)

## if statements

```py
if condition:
    Action

click = False

Like = 0

click = True

if click == True: ## mind you the double =; it's for checking
    Like += 1
    click = False

print(Like)
```

## Lists

```py
TestList = ["element1", "element2", "element3"]

# lists are zero indexed

Scores = [70, 85, 67.5, 90, 80]
print(Scores[0]) # output 70
print(Scores[-1]) # last element - 80
# accessing multiple numbers
print(Scores[0:2]) # 70,85
# start on X upto, NOT INCLUDING
print(Scores[2:]) # all the numbers to the end - 67.5, 90, 80
Scores[0] = 75 # change a value
Scores[1:3] = [] # remove values
Scores[2] = ["Hello", "world"]
print(Scores[2][0]) # Hello
Scores.append(82) # append to the end
```

## For loops

```py
Word = "Hello"

for w in Word: # w is the variable, what iterates (?)
	print(w) # print outputs everything and adds a new line
	if w == "e":
		print("what a funny letter")
```








