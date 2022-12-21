import telebot 
import datetime, time

#Atribuindo Chave do bot em uma variavel
api_key = "5699899917:AAFMgm4zV-vKDAHKF4usTq9ijvUqtEBilTM"

#Inicializando bot de acordo com a key
bot = telebot.TeleBot(api_key)

#Mensagens Padrão

#Fim de semana
text_weeknd = """
Sinto muito, nossos dias de funcionamento são:

Segunda-feira;
Terça-feira;
Quarta-feira;
Quinta-feira;
Sexta-feira; 

Fim de semana e feriado, atendimento apenas em nossas franquias!
Voltar ao inicio - /Inicio 
"""
#Cardápio Fit

fit_segunda = [["Carne de Sol, arroz, feijão carioca, legumes salteados e salada","Carboidratos: 150g | Proteinas: 150g | Fibra: 100g"],["Macarrão com molho de tomate e almôndega de carne","Carboidratos: 200g | Proteinas: 100g | Fibra: 20g"]]
fit_terca = [["Frango grelhado, arroz colorido, legumes salteados e salada","Carboidratos: 139g | Proteinas: 160g | Fibra: 100g"],["Macarrão ao alho e oleo e iscas de frango","Carboidratos: 200g | Proteinas: 110g | Fibra: 15g"]]
fit_quarta = [["Costela cozida, arroz, feijão carioca, legumes salteados e salada","Carboidratos: 170g | Proteinas: 143g | Fibra: 100g"],["Paqueca de frango com legumes salteados","Carboidratos: 170g | Proteinas: 180g | Fibra: 90g"]]
fit_quinta = [["Costela de porco, arroz com ervilha, legumes salteados","Carboidratos: 146g | Proteinas: 129g | Fibra: 100g"],["Salada verde com crotons e frango em cubos","Carboidratos: 100g | Proteinas: 180g | Fibra: 150g"]]
fit_sexta = [["Risoto de camarão com aspargos","Carboidratos: 130g | Proteinas: 115g | Fibra: 98g"],["Salada de mix de folhas, frango em cubos e legumes cozidos","Carboidratos: 150g | Proteinas: 150g | Fibra: 130g"]]

#Cardápio Low

low_segunda = ["Macarrão de abobrinha a bolonhesa","Carboidratos: 60g | Proteinas: 100g | Fibra: 50g"]
low_terca = ["Escondidinho de carne","Carboidratos: 90g | Proteinas: 130g | Fibra: 80g"]
low_quarta = ["Sanduiche natural de atum","Carboidratos: 65g | Proteinas: 90g | Fibra: 150g"]
low_quinta = ["Tiras de frango com molho especial","Carboidratos: 30g | Proteinas: 150g | Fibra: 100g"]
low_sexta = ["Quibe assado","Carboidratos: 69g | Proteinas: 150g | Fibra: 100g"]

#Cardápio ZeroLactose

zero_segunda = ["Nhoque de abóbora com molho caseiro","Carboidratos: 190g | Proteinas: 30g | Fibra: 70g"]
zero_terca = ["Omelete de frango e tomate confit","Carboidratos: 80g | Proteinas: 170g | Fibra: 80g"]
zero_quarta = ["Beringela recheada com frango e especiarias","Carboidratos: 60g | Proteinas: 110g | Fibra: 90g"]
zero_quinta = ["Bolinho de abobora e cenoura","Carboidratos: 150g | Proteinas: 30g | Fibra: 90g"]
zero_sexta = ["Salada verde com legumes e frango em cubos","Carboidratos: 120g | Proteinas: 90g | Fibra: 80g"]

#Comando Opções
@bot.message_handler(commands = ["Opcao1"])
def opcao1(message):
    pass

@bot.message_handler(commands = ["Opcao2"])
def opcao2(message):
    pass

#Comando Fit
@bot.message_handler(commands = ["Fit"])
def fit(message):
    
    day = datetime.date.today().weekday()
    #Fim de semana
    if day == 5  or day == 6:
        bot.send_message(message.chat.id, text_weeknd)
    #Segunda
    if day == 0:
        text_fit_segunda = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 
2.  Prato 2: {2}  
    Tabela Nutricional: {3}

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Prato 2: /Opcao2
Voltar ao inicio: /Inicio""".format(fit_segunda[0][0], fit_segunda[0][1], fit_segunda[1][0], fit_segunda[1][1])
        bot.send_message(message.chat.id, text_fit_segunda)
    #Terça
    if day == 1:
        text_fit_terca = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 
2.  Prato 2: {2}  
    Tabela Nutricional: {3}

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Prato 2: /Opcao2
Voltar ao inicio: /Inicio""".format(fit_terca[0][0], fit_terca[0][1], fit_terca[1][0], fit_terca[1][1])
        bot.send_message(message.chat.id, text_fit_terca)
    #Quarta
    if day == 2:
        text_fit_quarta = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 
2.  Prato 2: {2}  
    Tabela Nutricional: {3}

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Prato 2: /Opcao2
Voltar ao inicio: /Inicio""".format(fit_quarta[0][0], fit_quarta[0][1], fit_quarta[1][0], fit_quarta[1][1])
        bot.send_message(message.chat.id, text_fit_quarta)
    #Quinta
    if day == 3:
        text_fit_quinta = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 
2.  Prato 2: {2}  
    Tabela Nutricional: {3}

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Prato 2: /Opcao2
Voltar ao inicio: /Inicio""".format(fit_quinta[0][0], fit_quinta[0][1], fit_quinta[1][0], fit_quinta[1][1])
        bot.send_message(message.chat.id, text_fit_quinta)
    #Sexta
    if day == 4:
        text_fit_sexta = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 
2.  Prato 2: {2}  
    Tabela Nutricional: {3}

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Prato 2: /Opcao2
Voltar ao inicio: /Inicio""".format(fit_sexta[0][0], fit_sexta[0][1], fit_sexta[1][0], fit_sexta[1][1])
        bot.send_message(message.chat.id, text_fit_sexta)

#Comando LowCarb

@bot.message_handler(commands = ["LowCarb"])
def lowcarb(message):
    day = datetime.date.today().weekday()
    #Fim de semana
    if day == 5  or day == 6:
        bot.send_message(message.chat.id, text_weeknd)
    #Segunda
    if day == 0:
        text_lowc_segunda = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(low_segunda[0], low_segunda[1])
        bot.send_message(message.chat.id, text_lowc_segunda)
    #Terça
    if day == 1:
        text_lowc_terca = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(low_terca[0], low_terca[1])
        bot.send_message(message.chat.id, text_lowc_terca)
    #Quarta
    if day == 2:
        text_lowc_quarta = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(low_quarta[0], low_quarta[1])
        bot.send_message(message.chat.id, text_lowc_quarta)
    #Quinta
    if day == 3:
        text_lowc_quinta = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(low_quinta[0], low_quinta[1])
        bot.send_message(message.chat.id, text_lowc_quinta)
    #Sexta
    if day == 4:
        text_lowc_sexta = """
Ótima escolha!!

Hoje temos duas opções de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(low_sexta[0], low_sexta[1])
        bot.send_message(message.chat.id, text_lowc_sexta)

#Comando ZeroLact

@bot.message_handler(commands = ["ZeroLact"])
def zerolact(message):
    pass

#Verificador de recebimento de mensagem
def verify(message):
    return True

#Mensagem de bem vindo e Menu inicial
@bot.message_handler(func=verify)
@bot.message_handler(commands=["Inicio"])
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