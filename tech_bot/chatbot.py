from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot("home_bot", storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

for i in range(1,90000000000000):
    user_input = input()
    response = chatbot.get_response(user_input)
    print(response)
    i += 1

