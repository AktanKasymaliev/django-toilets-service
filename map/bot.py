# import telebot
# from . import views
#
#
#
# TOKEN = '1747778594:AAFMF4fUEJmD5qaDjQK5fo10Iymb_tMUJyA'
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def send_message(message):
# 	bot.reply_to(message, views.validating(request))
#
#
#
# bot.polling()