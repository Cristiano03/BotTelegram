import telebot

from Constants import APY_KEY

bot = telebot.TeleBot(APY_KEY, parse_mode=None)

@bot.message_handler(commands=["Ciao", "Aiuto"])
def send_help_message(msg):
    bot.reply_to(msg, "Ma chi ti vuole")

bot.polling()