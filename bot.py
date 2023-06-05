import telebot
from telebot import types

TOKEN ='6194826294:AAFRhYAD1A3Ec-BbURNjbD16LHBvmcpLaB4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Кнопка 1')
    item2 = types.KeyboardButton('Кнопка 2')
    item3 = types.KeyboardButton('Кнопка 3')
    item4 = types.KeyboardButton('Кнопка 4')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Hello, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, 'Это кнопка')

        elif message.text == 'Кнопка 2':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кнопка')
            back = types.KeyboardButton('Кнопка назад')
            markup.add(item1, back)

            bot.send_message(message.chat.id, 'Это просто кнопка', reply_markup=markup)

        elif message.text == 'Кнопка 3':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('How are you?')
            item2 = types.KeyboardButton('What is your name?')
            back = types.KeyboardButton('Кнопка назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Это кнопка3', reply_markup=markup)

        elif message.text == 'Кнопка 4':
            bot.send_message(message.chat.id, 'Это просто кнопка')

        elif message.text == 'Кнопка назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кнопка 1')
            item2 = types.KeyboardButton('Кнопка 2')
            item3 = types.KeyboardButton('Кнопка 3')
            item4 = types.KeyboardButton('Кнопка 4')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Кнопка назад'.format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)