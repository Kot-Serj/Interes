import telebot
from telebot import apihelper
import config


bot = telebot.TeleBot(config.token)
apihelper.proxy = {'http': config.proxy}


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('👕Футболки', '👖Джинсы')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, ты написал мне /start\nВыберай что ты хочешь', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Вот что я могу:')
    bot.send_message(
        message.chat.id, "1)ломаться на ровном месте\n2)быть не актиным\n3)Говорить 1 фразу")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '👕Футболки':
        bot.send_message(message.chat.id, 'Держи футболку 👕')
    elif message.text == '👖Джинсы':
        bot.send_message(message.chat.id, 'Держи джинсы 👖')


bot.polling()


#токен и прокси в папке Config.py

