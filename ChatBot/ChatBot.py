from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Bot')

conversa = ['Oi', 'Olá', 'Você gosta de mim?', 'Sim, você é meu criador']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    print('Bot: ', resposta)
