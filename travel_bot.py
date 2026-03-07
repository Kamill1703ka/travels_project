import telebot
from config import TOKEN
from bot.handlers import register_handlers

bot = telebot.TeleBot(TOKEN)

register_handlers(bot)

print("Бот запущен...")

bot.polling()