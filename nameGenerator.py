import csv
import random

with open('firstNamesScotland.csv', encoding='mac_roman') as namesDocument:
    reader = csv.reader(namesDocument)
    namesList = list(reader)

    quantity = len(namesList) - 1

    girlsFirstNames = []

    i = 4
    while i < quantity:
        girlsFirstNames.append(namesList[i][3])
        i = i + 1

    print(len(girlsFirstNames))

    def retrieveGirlsFirstName():
        randNum = random.randrange(0,len(girlsFirstNames))

        return girlsFirstNames[randNum]



print(retrieveGirlsFirstName())