import csv
import fileinput
import random


def cleanChar(fileName, str1, str2):
    with fileinput.FileInput(fileName, inplace=True) as file:
        for line in file:
            print(line.replace(str1, str2), end="")   


""" 
------------------------------------
    DIFFERENT WAY TO CLEAN FILES
------------------------------------
def pickWords(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    listWords = []
    for l in lines:
        l = l.replace("\n", "")
        l = l.replace("\t", "")
        listWords.append(l.split(" "))
    return listWords
""" 
        
        
finalList = []
def createList(fileName):
    with open(fileName,"r") as fileLocation:
        fileReader = csv.reader(fileLocation)        
        for line in fileReader:
            finalList.append(line)
    
    return finalList