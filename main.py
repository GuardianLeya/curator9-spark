import telebot

bot = telebot.TeleBot('6779239492:AAEHVK2DPKLCbNEqb6yioRjN7EOcU7vpsLU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, '*Привет,*\n _Как дела?_',  parse_mode='Markdown')

bot.infinity_polling()