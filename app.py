from modules import formatFile, game, getFiles
import os, random, urllib


def startGame():        

    listCategory = ["Animal", "Car", "Nouns"]
    chooseCategory = random.choice(listCategory)

    if chooseCategory == "Animal":
        animalGuess = random.choice(
            formatFile.createList("library/animals.csv"))
        game.playGame(chooseCategory, animalGuess)
    elif chooseCategory == "Car":
        carGuess = random.choice(formatFile.createList("library/cars.csv"))
        game.playGame(chooseCategory, carGuess)
    else:
        wordGuess = random.choice(
            formatFile.createList("library/nounlist.txt"))
        game.playGame(chooseCategory, wordGuess)

try:
    if urllib.request.urlopen("http://google.com"):
        try:
            gameFiles = [os.getcwd() + "/library/animals.csv", os.getcwd() + "/library/cars.csv", os.getcwd() + "/library/nounlist.txt"]
            for i in range(3):
                open(gameFiles[i], "r")
            startGame()
        except:
            getFiles.scrapFormatFiles()
            startGame()
except:
    print("\nNo internet connection needed to run the game for the first time.")