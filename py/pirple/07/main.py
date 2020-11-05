# Details:
 
# Return to your first homework assignments, when you described your favorite song. Refactor that code so all the variables are held as dictionary keys and value. Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.


# Extra Credit:

# Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. This function should accept two parameters: Key and Value. If the key exists in the dictionary and that value is the correct value, then the function should return true. In all other cases, it should return false.

song1 = {
        "Artist":"Tool",
        "Genre": "Progressive Metal",
        "SongName":"Parabol/a",
        "YearReleased":"2001",
        "Album":"Lateralus",
        "DurationInSeconds":"608",
        "Voice":"Maynard James Keenan",
        "Bass":"Justin Chancellor",
        "Guitar":"Adam Jones",
        "Battery":"Danny Carey",
        "AlbumCoverArtist":"Alex Grey",
        "AlbumURL":"https://toolband.com/releases/lateralus/",
        "Comments":"Best Song Ever. Period",
        "Favourite":True,
        }

def mySong(song):
    for value in song:
        print(value, ':', song[value])
    return

mySong(song1)


def guessingGame(song):
    polaco = 1
    while polaco == 1:
        fuess = input("Guess any information about the best song EVER:\n")
        if fuess in song.values():
            polaco = 0
            print("Correct!")
            break
        else:
            print("Not in the song metadata, please, try again")
            polaco = 1 
    return print("End Game")

guessingGame(song1)

