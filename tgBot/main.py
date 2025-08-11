import telebot

bot = telebot.TeleBot("8203033092:AAEhdT1Id69ImYWKA-VDuLVMKo76kyLW8HY")

@bot.message_handler(commands=["start"])
def send_start_mes(message):
    bot.send_message(message.chat.id, "Привет - это набросок")