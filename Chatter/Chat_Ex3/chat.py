from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious',
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, mas ainda não sou capaz de responder esta questão.',
            'maximum_similarity_threshold': 0.80
        }
    ])

#Utilizar um Corpus com um conjunto de frases para o Treinamento do Bot
trainer = ChatterBotCorpusTrainer(chatbot)

#Utilizar o corpus para português
trainer.train("chatterbot.corpus.portuguese")

print("Bot pronto! Converse com ele. Para encerrar digite 'tchau'")
frase = input("Eu: ")
while frase.find("tchau") < 0 and frase.find("TCHAU") < 0:
    print(frase)
    response = chatbot.get_response(frase)
    print("Bot:",response)
    frase = input("Eu: ")

response = chatbot.get_response("Tchau")
print("Bot:",response)
