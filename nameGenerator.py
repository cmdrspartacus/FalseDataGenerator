import csv
import pprint

with open('firstNamesScotland.csv', encoding='mac_roman') as namesDocument:
    reader = csv.reader(namesDocument)
    namesList = list(reader)

    quantity = len(namesList) - 1



    i = 10
    while i < 150:
        print(namesList[i][3])
        i = i + 1



