from bs4 import BeautifulSoup
import requests


def loadPage(url, tag):
    pageUrl = url
    pageRequest = requests.get(pageUrl).text
    pageContent = BeautifulSoup(pageRequest, "html.parser")
    pageResult = pageContent.find_all(tag)
    return pageResult


def addToFile(collection, fileName):
    for items in collection:
        if items.text.rstrip() != "":
            fileName.write(items.text + ",")