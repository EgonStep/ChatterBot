from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Cria um chatbot com nome Charlie
chatbot = ChatBot('Charlie')

#Define que o Treinador será do tipo ListTrainer(Os dados de treino serão passados via Lista)
trainer = ListTrainer(chatbot)

#Define os parâmetros do Treino
trainer.train([
    "Olá, posso ajudá-lo?",
    "Claro. Gostaria de reservar um voo para Recife",
    "Seu voo está reservado!"
])

# Recebe uma resposta para a entrada 'Gostaria de reservar um voo.'
response = chatbot.get_response('Gostaria de reservar um voo.')

print(response)