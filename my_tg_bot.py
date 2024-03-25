import telebot
from random import *
import json
import requests

neural_network_info = []  

# Функция для сохранения списка информации о нейронных сетях в файл JSON
def save():
    with open("neural_network_info.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(neural_network_info, ensure_ascii=False))
    print("Наша библиотека информации о нейросетях была успешно сохранена в файле neural_network_info.json")


# Функция для загрузки списка информации о нейронных сетях из файла JSON
def load():
    neural_network_info.clear()  # Очистка существующего списка для избежания дублирования записей при запуске бота
    with open("neural_network_info.json", "r", encoding="utf-8") as fh:
        neural_network_info.extend(json.load(fh))  # Используем extend для добавления элементов из загруженных данных в список
    print("Библиотека информации о нейросетях была успешно загружена")

API_TOKEN = '7184748465:AAG2BL8XIW0p1dWUtKNyWVhFWVXT7k_q-QQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Библиотека информации о нейросетях была успешно загружена!")

    except:
        neural_network_info.append("Нейросети в медицине")  
        neural_network_info.append("Обучение глубоких нейронных сетей")
        neural_network_info.append("Применение нейросетей в финансах")
        neural_network_info.append("Генеративно-состязательные сети")
        neural_network_info.append("Нейронные сети в автомобильной промышленности")
        bot.send_message(message.chat.id, "Библиотека была загружена по умолчанию!")

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"Вот список нейросетей")
    bot.send_message(message.chat.id, ", ".join(neural_network_info))
# Rоманда для получения случайной информации о нейросетях
@bot.message_handler(commands=['random'])
def show_random(message):
    random_info = choice(neural_network_info)
    bot.send_message(message.chat.id, f"Вот случайная информация о нейросетях для вас:\n{random_info}")

bot.polling()
