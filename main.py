import telebot
from telebot import types

bot = telebot.TeleBot("2104504379:AAELeMPUYj3i20MXd8DFblKyk-W7tfSjFFQ")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/inf", "/help","/open")
    bot.send_message(message.chat.id, 'Привет! '
                                      'Если хочешь узнать,что я умею, напиши: /help'.format(message.from_user,bot.get_me()),parse_mode='html', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message (message):
    bot.send_message(message.chat.id, "Я могу рассказать, где находится МТУСИ. Нажми кнопку '/inf'."
                                      "Дать ссылку на личный кабинет, для этого нужно написать 'личный кабинет'."
                                      "Рассказать когда у нас день открытых дверей, напиши команду '/open'."
                                      "Ознакомить с расписанием занятий, напиши 'расписание'")
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == '/inf':
        bot.send_message(message.chat.id, 'https://mtuci.ru/')
    if message.text.lower() == "личный кабинет":
        bot.send_message(message.chat.id, 'https://lms.mtuci.ru/lms/login/index.php')
    if message.text.lower() == "Личный кабинет":
        bot.send_message(message.chat.id, 'https://lms.mtuci.ru/lms/login/index.php')
    if message.text.lower() == "/open":
        bot.send_message(message.chat.id, "Уважаемые абитуриенты и их представители!Сообщаем Вам что 12 декабря 2021 года МТУСИ проводит день открытых дверей в очном формате, мероприятие будет проходить в два потока 11:00 и 13:00, зарегистрироваться можно на сайте, пройдя по ссылке:https://abitur.mtuci.ru/news/?ELEMENT_ID=5222"
                                          "Вход в здание осуществляется для лиц старше 18 лет по QR — коду вакцинации или ПЦР — теста (действительный в течение трёх дней)."
                                          "Ждем Вас 12 декабря 2021!"
                                          "При себе иметь билет в электронном или распечатанном виде!")

    if message.text.lower() == "расписание":
        bot.send_message(message.chat.id, 'https://mtuci.ru/time-table/')
    if message.text.lower() == "Расписание":
        bot.send_message(message.chat.id, 'https://mtuci.ru/time-table/')

bot.polling()
