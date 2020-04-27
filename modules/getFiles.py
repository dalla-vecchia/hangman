from modules import dataExtractionWeb as de
from modules import formatFile
import requests
from os import path
import fileinput
import csv


def scrapFormatFiles():
    # ----------------
    # ANIMALS SCRAPING
    # ----------------
    animalsFile = open(path.expanduser(
        "~") + "/projects/python/dev/hangman/library/animals.csv", "w")
    wildAnimals = de.loadPage(
        "https://7esl.com/wild-animals-vocabulary-english/", "h4")
    de.addToFile(wildAnimals, animalsFile)
    birds = de.loadPage("https://7esl.com/birds-vocabulary-english/", "h4")
    de.addToFile(birds, animalsFile)
    mamals = de.loadPage(
        "https://7esl.com/animal-vocabulary-english-mammals/", "h4")
    de.addToFile(mamals, animalsFile)
    animalsFile.close()
    # ---------------------------
    # FORMAT ANIMALS FILE FOR USE
    # ---------------------------
    formatFile.cleanChar("library/animals.csv", ",", "\n")
    formatFile.cleanChar("library/animals.csv", "\xa0", "")

    # ------------------------
    # CAR MANUFACTURE SCRAPING
    # ------------------------
    carsFile = open(path.expanduser("~") +
                    "/projects/python/dev/hangman/library/cars.csv", "w")
    cars = de.loadPage(
        "https://www.searchify.ca/keyword-list-car-brands/", "em")
    de.addToFile(cars, carsFile)
    carsFile.close()
    # ------------------------
    # FORMAT CARS FILE FOR USE
    # ------------------------
    formatFile.cleanChar("library/cars.csv", ",", "")

    # -----------------------------------
    # NOUNS ENGLISH WORDS - DOWNLOAD FILE
    # -----------------------------------
    with open("library/nounlist.txt", "wb") as file:
        response = requests.get(
            "http://www.desiquintans.com/downloads/nounlist/nounlist.txt")
        file.write(response.content)
