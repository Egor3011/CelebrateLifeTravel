import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def send_start_mes(message):
    bot.send_message(message.chat.id, "Привет - это набросок")