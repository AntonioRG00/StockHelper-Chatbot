class Component:
    def __init__(self, name, price, url, type):
        self.name = name
        self.price = price
        self.url = url
        self.type = type

    def __str__(self):
        return "Nombre: " + self.name + ", Precio: " + self.price + ", Url: " + self.url
    
class MainFunctions:
    def __init__(self, apiUrlRead, apiUrlWrite):
        self.apiUrlRead = apiUrlRead
        self.apiUrlWrite = apiUrlWrite
        
    def classify(self, text):
        import requests
        response = requests.get(self.apiUrlRead, params={ "data" : text })

        if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            return topMatch
        else:
            response.raise_for_status()

    def store(self, text, label):
        import requests
        response = requests.post(self.apiUrlWrite, json={ "data" : text, "label" : label })

        if response.ok:
            print ("Entiendo, que bien aprender de tí :)")
            return response.json()
        else:
            response.raise_for_status()
            
    def xmlToDict(self, xml):
        import xmltodict
        dict = xmltodict.parse(xml)
        
        finalDict = {}
        finalDict["texto"] = str(dict["componentes"]["texto"])
        finalDict["descripcion"] = str(dict["componentes"]["descripcion"])
        finalDict["componentes"] = [Component(x["nombre"], x["precio"], x["enlace"], x["tipo"]) for x in dict["componentes"]["componente"]]
        
        return finalDict