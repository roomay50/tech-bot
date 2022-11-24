# tech-bot
## a smart chatbot built using machine learning and natural language processing.

This project is a simple chatbot writen in python. it was trained to give information about the latest technologies
This project contains The following:

* intents.json: This is a file written in json. it stores specific communication responses which allows tech-bot answer questions or communicate within its purpose.
* main.py: This file uses NLP to sort out words from your intent file and group them into tags in your bag of words. it also contains the data that you train your model on.
* tech_bot_model.py: This is the model we train our data on. it is written using tensorflow's keras model. i think in the future, as the size of my intent file increases, i will like to train tech-bot using scikitlearn's built in neural networks model
* extract_funcs.py: This file contains functions that can extract specific information from the main.py file and other files in the project. These functions are also used  to introduce data into the  tech_bot gui.
* techbot_gui.py: This contains the code for the gui app built with tkinter. It is the users interface.
* reruirements.txt: This is a text file that contains all the libraries installed, and required for the project to work

## How to install and use tech-bot:
*1. clone this project: git clone ...
*2. install the requirements: pip install -r requirements.txt
*3. 
