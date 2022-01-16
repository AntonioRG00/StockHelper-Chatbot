import requests
import csv
import threading

def storeTraining(label, text):
    key = "5e533b50-76f9-11ec-81c5-e1cdfa92f93cc2df084c-c789-49ac-8839-eddcc0d946d1"
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