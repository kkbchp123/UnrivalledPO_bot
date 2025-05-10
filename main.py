
import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey there! I'm your Pocket Option signal bot.")

def send_signal(signal):
    bot.send_message(CHAT_ID, signal)

# Example signal on startup (you can remove this line later)
send_signal("Buy EUR/USD - EMA Cross confirmed!")

bot.polling()
