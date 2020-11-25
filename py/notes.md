# Python

Computer programming is the act of composing the selected programming language's elements in the order that will cause the desired effect.

There are two different ways of transforming a program from a high-level programming language into machine language:

1. compilation: the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing teh machine code; now you can distribute the file worldwide; the program that performs this translation is called a compiter or translator;
2. interpretation: you can translate the source program each time it has to be run; the progrma performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed; it also means that you cannot just distribute the source code as-is, because the end user needs the interpreter to execute it.


```py
def FunctionName(input):
    action
    return output
```

if it is indented, it's part of the function

```py
def addOne(Number):
    Number += 1
    return print(Number)

addOne(4)
```

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

Letters = []

for w in Word: # w is the variable, what iterates (?)
	print(w) # print outputs everything and adds a new line
	if w == "e":
		print("what a funny letter")
	Letters.append(w) # appends value of variable to the end on a list

print(Letters)

# Output: ['H', 'e', 'l', 'l', 'o']

for l in Letters:
  print(l)

Numbers = [1, 2, 3, 4, 5]

for i in Numbers:
  if 1%2 == 0;
    print("Par", i)
  else:
    print("impar", i)

# range(start, stopping, steps|increments) upto but not including stopping value
# default(optional_1, mandatory, optional_1)

for num in range(10):
  print(num)

# output: 0
#1
#2
#3
#4
#5
#6
#7
#8
#9

Numbers = []

for num in range(1,10,2):
  Numbers.append(num)
  print(num)

print(Numbers)
```

## While loops


```py
#while (condition):
#  Action
  
counter = 1
Sum = 0

while (counter <=10):
  # print(counter)
  Sum = Sum + counter
  counter += 1

print(Sum)

Letters = ['a, 'b', 'c', 'd', 'e',]

Index = 0

while (Index < len(Letters)):
  print(Index)
  print(Letters[index])
  Index += 1

height = 5000
velocity = 50
time = 0

while (height > 0 ):
  height = height - velocity
  time += 1

print(height)
print(time)
```

## Breaking and continuing loops


```py
Participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
position = 0

for name in Participants:
  if name == "Tina":
    print("About to break")
    break
  print("About to increment")
  position += 1

print(position)
# Once it reaches the break point it stops

for i in range(len(Participants)):
  if Participants[i] == "Joe":
    break
print(i)
# we can use the variable declared in the for loop
# When we reach a breaking point in a loop, the program doesn't execute anything after it

for number in range(10):
  if number%3 == 0:
    print(number, 'divisible by 3')
    Continue
  print('Not divisible by 3')
          
```

## Making Shapes with loops


```py
Length = 10

for pos in range(1,Lenght+1):
  print("c"*pos)

# c
# cc
# ccc
# cccc
# ccccc
# cccccc
# ccccccc
# ...

Length = 10
ToPrint = "a"

for pos in range(1,Length+1):
  print(ToPrint*pos)

for pos in range(Length-1, 0,-1):
  print(ToPrint*pos)

# a
# aa
# aaa
# aaaa
# aaa
# aa
# a

```

## Nested Loops


```py


for row in range(5):
  if row%2 == 0:
    for column in range(1,6):
      if column % 2 == 1:
	if column != 5:
	  print(" ",end="")
	else:
	  print(" ")
      else:
	print("|")
    #print(" | | ")
    #      12345 
  else:
    print("-----")


```

## Dictonaries and Sets


```py

Sets = {"element1", "element2", "element1"}

# elements remove repeated elements
# repetition of elements are removed
# sets don't have a specified order - we only want to know if it's there

if "element1" in Sets:
  print("yes")

CountryList = []

for i in range(5):
  Country = input("enter your country: ")
  CountryList.append(Country)

CountrySet = set(CountryList)
print(CountryList)
print(CountrySet)

# set() --> keyword - turns a datatype into a set

if "Brazil" in CountrySet:
  print("attended")

# Dictionaries

dictionary = {"key":"value", "key2":"value"}

# values in dictionaries are unique

CountryDictionary = {}
for Country in CountryList:
  if Country in CountryDictionary:
    CountryDictionary[Country] += 1
  else:
    CountryDictionary[Country] = 1

print(CountryDictionary)
# output (after input of 5 countries)
# CountryDictionary[Country] --> creates a key value pair OR adds something
# to the variable. instead of using the brackets to check the indexes of 
# values, we use the brackets to check if the value exists (sth like this); 
# there is no order in parenthesis nor in sets

# EXAMPLE

BlackShoes = {42:2, 41:3, 40:4, 39:1, 38:0} # inventory, no order
# size:stock
while(True): #(True == True)
  purchaseSize = int(input('which shoe size would you like to buy?\n'))
  if purchaseSize < 0:
    break
  if BalckShoes[purchseSize] > 0:
    BalckShoes[purchaseSize] -= 1
    print(BackShoes)
  else:
    print('no shoe sizes', purchaseSize)
```

## Input and Output

```py
# to convert into a string
Name = input("What's your name?")
print = str(Name)
# to convert into an int
Age = input("How old are you?")
print = int(Age)


Scores = []

for i in range(5):
  value = float(input("Please, enter the score for student " + str(i+1) + ":\n"))
  Scores.append(value)

print(Scores)


# File = open("Filename","r", "a", "w", "r+" ) # "read", "append", "write", "read and write"
# File.close() # --> once finished with the file, be sure to close the file
# Writing: If the file exists, it will overwrite it; if it does not exists, it will create it
VacationSpots = ["Cordoba", "Buenos Aires", "San Juan", "Bariloche"]

VacationFile = open("VacationPlaces", "w")

for Spots in VacationSpots:
  VacationFile.write(str(Spots + ", " + "\n")) # HAS TO BE A STRING

VacationFile.close()

VacationFile = open("VacationPlaces", "r")

FirstLine = VacationFile.readline()
print(FirstLine)  # Cordoba
SecondLine = VacationFile.readline()
print(SecondLine) # Cordoba

for line in VacationFile:
 print(line)  # delete new line created with print: print(line, end="")
 # San Juan
 # Bariloche - the pointer moves along with us

#TheWholeFile = VacationFile.read()
#print(TheWholeFile())

VacationFile.close()

FinalSpot = "Villa La Angostura"

VacationFile = open("VacationPlaces", "a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces", "r")
for line in VacationFile:
  print(line, end = "")

VacationFile.close()

for i in range(5):
  with open("VacationPlaces"+str(i), "r") as VacationFile:
    for line in VacationFile:
      print(line, end="")

```

```py
def drawField(field):
  for row in range(5) #0, 1, 2, 3, 4
    if row%2 == 0:
      # print writing lines
      practicalRow  = int(row/2)
      for column in range(5): #0, 1, 2, 3, 4
	if column%2 == 0:
	  practicalColumn = int(column/2)
	  if column != 4:
	    print(field[practicalColumn][practicalRow], end= "")
	  else:
	    print(field[practicalColumn][practicalRow])
	else:
	  print("|", end = "")
    else:
      print("------")

Player = 1
currentField = [[" ", " ", " "], [" ", " ", " " ], [" ", " ", " "]]
drawField(currentField)
while(True): # True == True
  print("Players turn: ", Player)
  MoveRow = int(input("Please enter the row\n"))
  MoveColum = int(input("Please enter the column\n"))
  if Player == 1:
    # make move for player 1
    # is the value empty?
    if currentField[MoveColumn][MoveRow] == " ":
      currentField[MoveColumn][Moverow] = "X"
      Player = 2
  else:
    # make move for player 2
    if currentField[MoveColumn][MoveRow] == " ":
      currentField[MoveColumn][MoveRow] = "O"
      Player = 1
  drawField(currentField)
```

```py
ParticipantNumber = 5
participantData = []

resgisteredParticipants = 0

while ( resgisterParticipants < ParticipantNumber):
  tempPartData = [] # name, country of origin, age
  name = input('what's your name? ')
  country = input('where do you come from? ')
  age = int(input('how old are you? '))
  tempPartData.append(name, country, age)
  participantData.append(tempartData)
  
```

- used for both writing and reading a file: r+
- to open a file: myfile = open("myfile.txt", "r")
- myFile = open(file = "VacationPlaces","w")
- if we use open('test.txt') without r or w, we are opening a file for read only







