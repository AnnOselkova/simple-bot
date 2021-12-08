import telebot
from telebot import types

bot = telebot.TeleBot("2104504379:AAELeMPUYj3i20MXd8DFblKyk-W7tfSjFFQ")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "Help","адрес", "для абитуриентов", "личный кабинет студента")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def startmessage (message):
    bot.send_message(message.chat.id, 'адрес')
    bot.send_message(message.chat.id, 'для абитуриентов')
    bot.send_message(message.chat.id, 'личный кабинет студента')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "help":
        bot.send_message(message.chat.id, 'адрес')
        bot.send_message(message.chat.id, 'для абитуриентов')
        bot.send_message(message.chat.id, 'личный кабинет студента')
    if message.text.lower() == "адрес":
        bot.send_message(message.chat.id, 'https://mtuci.ru/sveden/contacts/')
    if message.text.lower() == "для абитуриентов":
        bot.send_message(message.chat.id, 'https://abitur.mtuci.ru/ ')
    if message.text.lower() == "личный кабинет студента":
        bot.send_message(message.chat.id, 'https://lms.mtuci.ru/lms/login/index.php')
bot.polling()