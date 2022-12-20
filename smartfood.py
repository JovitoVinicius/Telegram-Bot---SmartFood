import telebot 
import datetime, time

#Atribuindo Chave do bot em uma variavel
api_key = "5699899917:AAFMgm4zV-vKDAHKF4usTq9ijvUqtEBilTM"

#Inicializando bot de acordo com a key
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands = ["Fit"])
def fit(message):
    
    pass

@bot.message_handler(commands = ["LowCarb"])
def lowcarb(message):
    pass

@bot.message_handler(commands = ["ZeroLact"])
def fzerolact(message):
    pass
#Verificador de dia
def message_date():
    day = datetime.date.today()
    return day

#Verificador de recebimento de mensagem
def verify(message):
    return True

#Mensagem de bem vindo e Menu inicial
@bot.message_handler(func=verify)
def welcome_message(message):
    text = """
Olha só quem está por aqui!! Seja bem vind@ ao SmartFood <3

Olá {}, esperamos que esteja bem! 

Sua alimentação saudável começa aqui!

Eae, qual vai ser seu pedido de hoje?
1.Fazer pedido de marmita fit - /Fit
2.Fazer pedido de marmita low carb - /LowCarb
3.Fazer pedido de marmita zero lactose - /ZeroLact
    
Por favor responda com uma das opções acima para que possamos continuar com seu atendimento :)""".format(message.chat.first_name)
    bot.send_message(message.chat.id, text)

#Método utilizado para manter o bot sempre conversando com a API do Telegram, assim sempre recebendo as mensagens do usuário e realizando as funções necessárias.
bot.polling()