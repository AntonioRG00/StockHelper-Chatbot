import requests

class Component:
    def __init__(self, name, price, url, imageUrl):
        self.name = name
        self.price = price
        self.url = url
        self.imageUrl = imageUrl

    def __str__(self):
        return "Nombre: " + self.name + ",\nPrecio: " + self.price + ",\nUrl: " + self.url + ",\nImage: " + self.imageUrl

apiKey = "2580bc30-7550-11ec-9a35-e1f497862e67688776a5-1191-40c5-838d-7b029f14fc31"
apiUrlRead = "https://machinelearningforkids.co.uk/api/scratch/"+ apiKey + "/classify"
apiUrlWrite = "https://machinelearningforkids.co.uk/api/scratch/"+ apiKey + "/train"
myClassifications = {
    "procesador": [
        Component("Procesador Intel Core i7-10700K", "300€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Procesador Intel Core i7-8700K", "250€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Procesador Intel Core i7-8950H", "340€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Procesador Intel Core i7-11700K", "350€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
    ],
    "grafica": [
        Component("Grafica Nvidia GTX 1080 Ti", "500€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Grafica Nvidia GTX 1080", "400€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Grafica Nvidia GTX 1070", "300€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Grafica Nvidia GTX 1060", "200€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
    ],
    "ram": [
        Component("Ram Corsair Vengeance 16GB", "100€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Ram Corsair Vengeance 8GB", "80€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Ram Corsair Vengeance 4GB", "60€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
        Component("Ram Corsair Vengeance 2GB", "40€", "https://www.amazon.es", "https://images-na.ssl-images-amazon.com"),
    ]
}

def classify(text):
    response = requests.get(apiUrlRead, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def store(text, label):
    response = requests.post(apiUrlWrite, json={ "data" : text, "label" : label })

    if response.ok:
        print ("Entiendo, que bien aprender de tí :)")
        return response.json()
    else:
        response.raise_for_status()

def didntUnderstand(text):
    print("Vaya, no he entendido lo que me has dicho")
    label = input("Dime de cuales de estas temáticas me estás hablando " + str([x for x in myClassifications.keys()]) + ": ")
    if label in myClassifications.keys():
        store(text, label)
    else:
        didntUnderstand(text)

print("Saludos, soy un bot que te ayudará a encontrar los mejores componentes adaptado a tus necesidades")
print("Actualmente tenemos los siguientes componentes en el catálogo: " + str([x for x in myClassifications.keys()]))
while True:
    text = input("Dime que necesitas: ")

    result = classify(text)

    if(result["confidence"] > 75):
        print("Entiendo, quieres saber sobre", "\"" + result["class_name"] + "\"", "estoy preguntando al que más sabe!")
        print("He extraído la siguiente información:")
        print("\n".join([str(x) for x in myClassifications[result["class_name"]]]))
    elif(result["confidence"] > 35):
        didntUnderstand(text)
    else:
        print("No sé a que te refieres ni creo que me dedique a clasificar este tipo de cosas :(")