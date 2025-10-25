import telebot
import requests
import json
import random
from colorama import Fore, Style
import re

# === BOT TOKEN ===
BOT_TOKEN = "8208835169:AAGLoUJS4gFg6JnS8AeBIfz7A3XMDWvVIPA"  # 🔁 Replace with your bot token
API_BASE_URL = "https://demon.taitanx.workers.dev/" 
bot = telebot.TeleBot(BOT_TOKEN)
MOBILE_REGEX = r'\b(\d{10})\b'
CAR_REGEX = r'([A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4})'

# === START MESSAGE ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "\n\n👋 Welcome to *Info By Tufan [ Bot ]* ! \n\n"
        "🔍 Send your target mobile/car number \n"
        "_I will search for leaked data if available._\n\n"
        "👉 **Please try one of these formats:**\n\n"
        " ** Mobile Number: ** 9876543210 (10 digits only)\n\n"
        "** Car Number: ** DL1C1234 or MH12AB9012 \n\n"
        "🔴 * Created by @cyber_tufan * \n\n"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['admin'])
def send_welcome(message):
    welcome_text = (
        "🔴 *Created by @cyber_tufan *"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')



def fetch_mobile_details(mobile_number):
    try:
        details_text = f"**📱 Mobile Details for {mobile_number}:**\n\n"
        payload = {"mobile": mobile_number} 
        response = requests.get(API_BASE_URL, params=payload)
        response.raise_for_status() 
        try:
            data = response.json()
            if "credit" in data:
                data["credit"] = "@cyber_tufan"
            if "developer" in data:
                data["developer"] = "@cyber_tufan"
            beautified_json = json.dumps(data, indent=4, ensure_ascii=False)
            final_output = f"{details_text}```json\n{beautified_json}\n```"
            return final_output, True
        except json.JSONDecodeError:
            return f"**📱 Mobile Details for {mobile_number}:**\n\n*Raw API Response (Not JSON):*\n\n```\n{response.text[:1000]}\n```", True
    except requests.exceptions.RequestException as e:
        return f"❌ **API Error (Mobile):** Details nahi mil payi. Error: {e}", False




def fetch_car_details(car_number):
    try:
        details_text = f"**🚗 Car Details for {car_number}:**\n\n"
        payload = {"number": car_number} 
        response = requests.get(API_BASE_URL, params=payload)
        response.raise_for_status()
        try:
            data = response.json()
            if "credit" in data:
                data["credit"] = "@cyber_tufan"
            if "developer" in data:
                data["developer"] = "@cyber_tufan"
            beautified_json = json.dumps(data, indent=4, ensure_ascii=False)
            final_output = f"{details_text}```json\n{beautified_json}\n```"
            return final_output, True
        except json.JSONDecodeError:
            return f"**🚗 Car Details for {car_number}:**\n\n*Raw API Response (Not JSON):*\n\n```\n{response.text[:1000]}\n```", True
    except requests.exceptions.RequestException as e:
        return f"❌ **API Error (Car):** Details nahi mil payi. Error: {e}", False

# ----------------- General Message Handler -----------------

@bot.message_handler(content_types=['text'])
def all_message_checker(message):

    chat_id = message.chat.id
    text_processed = message.text.strip().upper().replace(" ", "")

    mobile_match = re.search(MOBILE_REGEX, text_processed)
    car_match = re.search(CAR_REGEX, text_processed)
    
    details_to_send = ""
    is_success = False

    if mobile_match:
        number = mobile_match.group(1)
        bot.send_message(chat_id,f" ꧁𓊈𒆜🆃🆄🅵🅰🅽𒆜𓊉꧂ \n\n 🔍 Searching details for {number} \n Please wait few seconds ... ", parse_mode="Markdown")
        details_to_send, is_success = fetch_mobile_details(number)
        
    elif car_match:
        number = car_match.group(1)
        bot.send_message(chat_id,f" ꧁𓊈𒆜🆃🆄🅵🅰🅽𒆜𓊉꧂ \n\n 🔍 Searching details for {number} \n Please wait few seconds ... ", parse_mode="Markdown")
        details_to_send, is_success = fetch_car_details(number)
        
    else:
        details_to_send = (
            "**🤖 Welcome to *Info By Tufan [ Bot ] * ! **\n\n"
            "Aapne koi valid Mobile Number ya Car Number nahi diya hai.\n\n"
            "👉 ** Please try one of these formats: ** \n\n"
            " ** Mobile Number: ** 9876543210 (10 digits only)\n\n"
            " ** Car Number: ** DL1C1234 or MH12AB9012 \n"
        )
        
    bot.send_message(chat_id, details_to_send, parse_mode="Markdown")



# @bot.message_handler(func=lambda message: message.text.startswith('Hey'), content_types=['text'])
#def handle_hey(message):
   # bot.reply_to(message, "I see you started your message with 'Hey'! How can I help you?")


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

# === RUN BOT ===
print("🤖 Bot is running...")
bot.infinity_polling()