import telebot
from telebot import types
import database as dt
import requests

import config as cfg

bot = telebot.TeleBot(cfg.BOT_TOKEN)

user_data = {}

@bot.message_handler(commands=["start"])
def send_start_mes(message):
    print(f"User {message.from_user.id} called command: {message.text}")

    if message.text != "/start":
        print(message.text[7:])
        text_after_start = message.text[7:].split("_")
        print(text_after_start)
        if text_after_start[0] == "id":
            user_data[message.chat.id] = {}
            print(user_data)

            response = requests.get(f"http://backend:8000/get_user_for_tg/{text_after_start[1]}")
            info = response.json()
            print(info)

            user_data[message.chat.id]["name"] = info["name"]
            user_data[message.chat.id]["phone"] = info["phone"]
            user_data[message.chat.id]["tour"] = info["tour"]

            show_contact_button_fromStart(message=message)
    elif message.text == "/start":
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


#для кнопки старт
def show_contact_button_fromStart(message):
    
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


@bot.message_handler(func=lambda message: message.text == "Связаться с менеджером")
def send_manager_message(message):
    print(user_data)
    userinfo = user_data[message.chat.id]
    dt.addNewUser(userinfo["name"], userinfo["phone"], userinfo["tour"])
    bot.send_message(message.chat.id, "Спасибо за ваше обращение! Мы свяжемся с вами в ближайшее время.", reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True)