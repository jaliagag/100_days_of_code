maxNumber = 2
participantData = []

#
outputFile = open("ParticipantData", "w") # if i don't have the file, it is created; INFORMATION IS OVERWRITTEN

registered = 0

while ( registered < maxNumber):
  tempPartData = [] # name, country of origin, age
  name = input("what's your name? ")
  country = input('where do you come from? ')
  age = int(input('how old are you? '))
  tempPartData.append(name)
  tempPartData.append(country)
  tempPartData.append(age)
  participantData.append(tempPartData)
  # print("##########")
  registered += 1

# print(participantData)

# writing to a file
# either at the end, or every time a participant is added

for participant in participantData:
    for data in participant:
        outputFile.write(str(data)) # we can only write strings
        outputFile.write(" ")
    outputFile.write("\n")

outputFile.close()

inputFile = open("ParticipantData", "r")

inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    # strip removes the parameter
    # split on strings, it splits it by default into spaces - ["joe", "arg", "31"]
    inputList.append(tempParticipant)

# Dictinary for age, how many times a specific age is repeated

Age = {}

for part in inputList:
    # -1 the last element in the array
    if part[-1] in Age:
        Age[part[-1]] += 1
        # into the Age dictionary
    else:
        Age[part[-1]] = 1 # if the valeu is not in the dictionary, it creates the value

Countries = {}

for part in inputList:
    # -1 the last element in the array
    if part[1] in Countries:
        Countries[part[1]] += 1
        # into the Age dictionary
    else:
        Countries[part[1]] = 1 # if the valeu is not in the dictionary, it creates the value

print(Age)
Oldest = 0

Youngest = 100
mostOccurringAge = 0
counter = 0

for tempage in Age:
    if int(tempage) > Oldest:
        Oldest = tempage
    if int(tempage) < Youngest:
        Youngest = tempage
    if Age[tempage] >= counter:
        counter = Age[tempage]
        mostOccurringAge = tempage

print(Oldest)
print(Youngest)
print('most occurring age is', mostOccurringAge,'with', counter,'participants')



inputFile.close()
