
import telebot
import requests

API_TOKEN = '7184748465:AAG2BL8XIW0p1dWUtKNyWVhFWVXT7k_q-QQ'
API_URL = ''  

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я готов помочь тебе узнать информацию о животных. Просто напиши мне название интересующего животного!")

@bot.message_handler(func=lambda message: True)
def get_animal_info(message):
    animal_name = message.text
    data = {'animal_name': animal_name}
    try:
        response = requests.get(API_URL, params=data).json()
        info = response.get('info')
        if info:
            bot.send_message(message.chat.id, info)
        else:
            bot.send_message(message.chat.id, "К сожалению, информация об этом животном не найдена.")
    except Exception as e:
        print(str(e))
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуй еще раз позже.")

bot.polling()