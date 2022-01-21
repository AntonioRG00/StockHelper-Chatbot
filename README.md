# StockHelper
This repository is about 3 chatbots made with AIML/ML4K.
The chatbots will try to classify which pc components we are talking about and give a answer with data related

## StockHelper-ML4K
This chatbot is made with ML4K and is dedicated to classifying 3 categories of pc components (Graphics card, Processor and RAM)

## StockHelper-AIML
This chatbot is made with AIML on pandorabots **(Not compatible with AIML standard because it has html labels)**
Is also dedicated to classifying the same 3 categories of pc componentes but with subcategories based on price and it has navigation.

![image](https://user-images.githubusercontent.com/60214254/149680219-4e62d869-7436-4b96-923e-6717c4fd57f3.png)

## StockHelper-Combined
This project combines the others in one. It does not have navigation but has the same categories and subcategories than the last one.
The ML4K part is in charge of translating the text (input by user) into the desired tag, which is then passed to the aiml bot so that it returns an xml with the catalog information.
