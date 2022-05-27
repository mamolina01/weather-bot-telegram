import telebot
from getClima import getClima
from variables import token

bot=telebot.TeleBot(token,parse_mode=None)

# /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, """
Bienvenido!
Desea obtener datos climaticos de su país?
Ingrese el comando /pais, y a continuación
el nombre de su país.
A continuación le dejamos un ejemplo.
/clima argentina
    """)


@bot.message_handler(commands=['clima'])
def clima(mensaje):
    chat_id = mensaje.chat.id
    mensaje = mensaje.text.split()[1::]
    pais=" ".join(mensaje)
    #respuesta="La temperatura de Argentina es: " + str(round(y["temp"]-273.15))
    bot.send_message(chat_id, getClima(pais))



@bot.message_handler()
def echo_all(message):
    chatId = message.from_user.id
    userMsg = message.text.lower()

    if("hola" in userMsg or "hi" in userMsg):
        bot.send_message(chatId, "Hola, como estas?")
    elif("chau" in userMsg):
        bot.send_message(chatId, "Chau, hasta luego!")
    elif("gracias" in userMsg):
        bot.send_message(chatId, "De nada")
    else:
        bot.send_message(chatId, "No entiendo. Si necesitas ayuda envia el comando /help")

bot.infinity_polling()