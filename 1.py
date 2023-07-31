# 5423961505:AAFF1llXP8Vb3MNcN8OpQlszwTl5ZbfuHRM

import telebot
from telebot import types

token='5423961505:AAFF1llXP8Vb3MNcN8OpQlszwTl5ZbfuHRM'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    biskvit_btn = types.InlineKeyboardButton(text="Бисквитные торты", callback_data='1')
    muss_btn = types.InlineKeyboardButton(text="Муссовые торты", callback_data='2')
    bento_btn = types.InlineKeyboardButton(text="Бенто-тортики", callback_data='3')
    narezka_btn = types.InlineKeyboardButton(text="Нарезные пирожные", callback_data='4')
    eskimo_btn = types.InlineKeyboardButton(text="Эскимо", callback_data='5')
    zakaz_btn = types.InlineKeyboardButton(text="Хочу заказать!", callback_data='6')
    keyboard.add(biskvit_btn)
    keyboard.add(muss_btn)
    keyboard.add(bento_btn)
    keyboard.add(narezka_btn)
    keyboard.add(eskimo_btn)
    keyboard.add(zakaz_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Мир сладостей",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('5.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Бисквитные торты. От 40р. за 1 кг",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('6.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Муссовые торты. От 36р. за 1 кг",
                reply_markup=keyboard)
            img.close()
        #  добавила свои кнопки
        if call.data == "3":
            img = open('7.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Бенто-торты. От 18р. за 0,5 кг",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('8.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Нарезные пирожные. От 3р. за 1 штуку",
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            img = open('9.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Эскимо. От 4,5р. за 1 штуку",
                reply_markup=keyboard)
            img.close()
        if call.data == "6":
            bot.send_message(chat_id=call.message.chat.id, text="Нажмите, для перехода в личные сообщения @piccola_by)")


if __name__=="__main__":
    bot.polling(none_stop=True)