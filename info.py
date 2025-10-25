import telebot
import requests
import json
import random
from colorama import Fore, Style

# === BOT TOKEN ===
BOT_TOKEN = "8208835169:AAGLoUJS4gFg6JnS8AeBIfz7A3XMDWvVIPA"  # 🔁 Replace with your bot token
bot = telebot.TeleBot(BOT_TOKEN)

# === START MESSAGE ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "👋 Welcome to *Info By Tufan Bot*\n\n"
        "🔍 Send your target number/email (e.g. +91********** or email@example.com)\n"
        "_I will search for leaked data if available._\n\n"
        "🔴 *Credit by @cyber_tufan *"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['admin'])
def send_welcome(message):
    welcome_text = (
        "🔴 *Create by @cyber_tufan *"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
	
@bot.message_handler(func=lambda message: message.text.startswith('Hey'), content_types=['text'])
def handle_hey(message):
    bot.reply_to(message, "I see you started your message with 'Hey'! How can I help you?")

# === RUN BOT ===
print("🤖 Bot is running...")
bot.infinity_polling()