import telebot
import time

# Токен получите у @BotFather
API_TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Привет, {name}! Я твой первый бот! 🚀")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Команды: /start, /help, /time"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = time.strftime('%H:%M:%S')
    bot.reply_to(message, f"Текущее время: {current_time}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

print("Бот запущен!")
bot.polling()
