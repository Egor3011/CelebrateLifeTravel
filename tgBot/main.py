import telebot
from telebot import types

import config as cfg

bot = telebot.TeleBot(cfg.BOT_TOKEN)

user_data = {}

@bot.message_handler(commands=["start"])
def send_start_mes(message):
    print(f"User {message.from_user.id} called command: {message.text}")
    if message.text == "/start":
        user_data[message.chat.id] = {}
        bot.send_message(message.chat.id, "Привет! Давай запишемся на тур. Как вас зовут?")
        bot.register_next_step_handler(message, ask_phone_number)

def ask_phone_number(message):
    user_data[message.chat.id]['name'] = message.text
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton("Поделиться номером телефона", request_contact=True)
    markup.add(button)

    bot.send_message(message.chat.id, "Отлично, " + message.text + ". Теперь поделись своим номером телефона, нажав на кнопку ниже.", reply_markup=markup)
    bot.register_next_step_handler(message, ask_tour_name)


def ask_tour_name(message):
    if message.contact:
        user_data[message.chat.id]['phone'] = message.contact.phone_number
        bot.send_message(message.chat.id, "Спасибо!", reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, "Пожалуйста, воспользуйтесь кнопкой 'Поделиться номером телефона'.")
        bot.register_next_step_handler(message, ask_tour_name)
        return


    markupTour = types.ReplyKeyboardMarkup() # Replace with actual manager username
    for i in cfg.TOURS:
        markupTour.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, "И последнее: как называется тур, который тебя интересует?", reply_markup=markupTour)
    bot.register_next_step_handler(message, show_contact_button)


def show_contact_button(message):
    try:
        user_data[message.chat.id]['tour'] = message.text
        
        markupEnd = types.ReplyKeyboardMarkup()
        button = types.KeyboardButton("Связаться с менеджером") # Replace with actual manager username
        markupEnd.add(button)

        summary = (
            f"Отлично, {user_data[message.chat.id]['name']}! \n"
            f"Ваш номер телефона: {user_data[message.chat.id]['phone']}\n"
            f"Интересующий тур: {user_data[message.chat.id]['tour']}\n\n"
            f"Нажми кнопку ниже, чтобы связаться с нашим менеджером."
        )
        bot.send_message(message.chat.id, summary, reply_markup=markupEnd)
    except Exception as ex:
        print(ex)


@bot.message_handler(func=lambda message: message.text == "Связаться с менеджером")
def send_manager_message(message):
    try:
        print(user_data)
        userinfo = user_data[message.chat.id]
        bot.send_message(message.chat.id, "Спасибо за ваше обращение! Мы свяжемся с вами в ближайшее время.", reply_markup=types.ReplyKeyboardRemove())
    except Exception as ex:
        print(ex)

bot.polling(none_stop=True)