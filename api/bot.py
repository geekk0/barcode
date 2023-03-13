import telebot

# Create bot
bot = telebot.TeleBot(token='5610845761:AAGUnzv5MqsMQT22G6yXNptcNZss7wbAMrk')

# Send message
# bot.send_message(123456798, 'Hi! I\'m a Bot!')


def send_telegram_order_notification(text):
    bot.send_message(-1001974047206, text)