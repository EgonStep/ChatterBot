from chatterbot import ChatBot


bot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

print("Crtl + Z & Enter Para fechar a aplicação.")
while True:
    try:
        question = input("Question: ")
        response = bot.get_response(question)
        print(response)
    except EOFError:
        break