import telebot 
import datetime, time

#Atribuindo Chave do bot em uma variavel
api_key = "5699899917:AAFMgm4zV-vKDAHKF4usTq9ijvUqtEBilTM"

#Inicializando bot de acordo com a key
bot = telebot.TeleBot(api_key)

#Variaveis Globais
day = 0
#day = datetime.date.today().weekday()
typefood = 0
#Variaveis de comida
quantidadefoodfit = 0
orderfit = [""]
pricefoodfit = 25.90
pricefoodtotalfit = 0

quantidadefoodlow = 0
orderlow = [""]
pricefoodlow = 23.90
pricefoodtotallow = 0

quantidadefoodzero = 0
orderzero = [""]
pricefoodzero = 26.90
pricefoodtotalzero = 0

#Variaveis de suco
quantidadejuice = 0
flavorjuice = [""]
pricejuice = 5.99
pricejuicetotal = 0
#Total
pricefinal = 0
#Comanda
comand = [quantidadefoodfit, orderfit, pricefoodtotalfit, quantidadefoodlow, orderlow, pricefoodtotallow, quantidadefoodzero, orderzero, pricefoodtotalzero, quantidadejuice, flavorjuice, pricejuicetotal, pricefinal]

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
Voltar ao inicio - /Inicio"""

#Quantidade
text_quantidade = """
Digite a quantidade que deseja:
"""

erro_quantidade = """
Favor digitar apenas em formato numérico. Exemplo: 2 
"""

#Comanda
text_comand = """
Pedido anotado com sucesso!

Aqui está o que você pediu!

    Comanda:
    Fit: {} x {} = {}
    Low Carb: {} x {} = {}
    Zero Lactose: {} x {} = {}                                   
    {} x Suco (Sabor: {}) = {}                          

    Valor de entrega: R$ 7,99

    Total do pedido + taxa de serviço (10%): {}

Deseja alterar o pedido? - /Alterar
Caso não tenha alteração, deseja concluir pedido? - /Concluir
Voltar ao inicio. - /Inicio""".format(comand[0], comand[1], comand[2], comand[3], comand[4],comand[5], comand[6], comand[7], comand[8], comand[9], comand[10], comand[11], comand[12])

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

#Comando Alterar
@bot.message_handler(commands = ["Alterar"])
def alterar(message):
    pass

#Comando Concluir
@bot.message_handler(commands = ["Concluir"])
def concluir(message):
    pass

#Comando Opções
@bot.message_handler(commands = ["Opcao1"])
def opcao1(message):

#Fit
    if typefood == 0:
        if day == 0:
            print(quantidadefoodfit)
            bot.send_message(message.chat.id, text_quantidade)
            quantidadefoodfit = message.text
            print(quantidadefoodfit)
            orderfit[0] = fit_segunda[0][0]
            
        if day == 1:
            orderfit[0] = fit_terca[0][0]
            
        if day == 2:
            orderfit[0] = fit_quarta[0][0]
            
        if day == 3:
            orderfit[0] = fit_quinta[0][0]
            
        if day == 4:
            orderfit[0] = fit_sexta[0][0]
            
 #Low
    if typefood == 1:
        if day == 0:
            orderlow[0] = low_segunda[0]
        if day == 1:
            orderlow[0] = low_terca[0]
        if day == 2:
            orderlow[0] = low_quarta[0]
        if day == 3:
            orderlow[0] = low_quinta[0]
        if day == 4:
            orderlow[0] = low_sexta[0]
 #Zero
    if typefood == 2:
        if day == 0:
            orderzero[0] = zero_segunda[0]
        if day == 1:
            orderzero[0] = zero_terca[0]
        if day == 2:
            orderzero[0] = zero_quarta[0]
        if day == 3:
            orderzero[0] = zero_quinta[0]
        if day == 4:
            orderzero[0] = zero_sexta[0]


@bot.message_handler(commands = ["Opcao2"])
def opcao2(message):
    pass

#Comando Fit
@bot.message_handler(commands = ["Fit"])
def fit(message):
    typefood = 0 #Fit = 0
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
def lowcarb(message, day, typefood):
    typefood = 1 #Low = 1
#Fim de semana
    if day == 5  or day == 6:
        bot.send_message(message.chat.id, text_weeknd)
#Segunda
    if day == 0:
        text_lowc_segunda = """
Ótima escolha!!

Hoje temos a seguinte opção de marmita:

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

Hoje temos a seguinte opção de marmita:

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

Hoje temos a seguinte opção de marmita:

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

Hoje temos a seguinte opção de marmita:

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

Hoje temos a seguinte opção de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(low_sexta[0], low_sexta[1])
        bot.send_message(message.chat.id, text_lowc_sexta)

#Comando ZeroLact

@bot.message_handler(commands = ["ZeroLact"])
def zerolact(message, day, typefood):
    typefood = 2 #Zero = 2
#Fim de semana
    if day == 5  or day == 6:
        bot.send_message(message.chat.id, text_weeknd)
#Segunda
    if day == 0:
        text_zero_segunda = """
Ótima escolha!!

Hoje temos a seguinte opção de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(zero_segunda[0], zero_segunda[1])
        bot.send_message(message.chat.id, text_zero_segunda)
#Terça
    if day == 1:
        text_zero_terca = """
Ótima escolha!!

Hoje temos a seguinte opção de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(zero_terca[0], zero_terca[1])
        bot.send_message(message.chat.id, text_zero_terca)
#Quarta
    if day == 2:
        text_zero_quarta = """
Ótima escolha!!

Hoje temos a seguinte opção de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(zero_quarta[0], zero_quarta[1])
        bot.send_message(message.chat.id, text_zero_quarta)
#Quinta
    if day == 3:
        text_zero_quinta = """
Ótima escolha!!

Hoje temos a seguinte opção de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(zero_quinta[0], zero_quinta[1])
        bot.send_message(message.chat.id, text_zero_quinta)
#Sexta
    if day == 4:
        text_zero_sexta = """
Ótima escolha!!

Hoje temos a seguinte opção de marmita:

1.  Prato 1: {0} 
    Tabela Nutricional: {1} 

Selecione a opção desejada para prosseguir no pedido:

Prato 1: /Opcao1
Voltar ao inicio: /Inicio""".format(zero_sexta[0], zero_sexta[1])
        bot.send_message(message.chat.id, text_zero_sexta)

#Verificador de recebimento de mensagem
def verify(message):
    return True

#Mensagem de bem vindo e Menu inicial
#@bot.message_handler(func=verify)
@bot.message_handler(commands=["Inicio"])
@bot.message_handler(commands=["start"])
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