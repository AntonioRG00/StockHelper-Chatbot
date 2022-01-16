import requests
import csv
import threading

def storeTraining(label, text):
    key = "f83fb2a0-762e-11ec-a354-837701a2e7a2c356802b-9914-45c3-b4f3-d99939efa674"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/train"

    print("Text:", text, "Label:", label)
    response = requests.post(url, json={ "data" : text, "label" : label })

    if response.ok == False:
        print (response.json())

def readCsvUTF8(fileName):
    with open(fileName, 'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

def storeDefaultQuestions():
    list = readCsvUTF8("questions.csv")
    allThreads = []
    for row in list:
        allThreads.append(threading.Thread(target=storeTraining, args=(row[0], row[1])))
        allThreads[-1].start()

storeDefaultQuestions()