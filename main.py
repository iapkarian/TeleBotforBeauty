import telebot
from telebot import types
import random
import os


TOKEN = '5540905952:AAHGS_pSaI6mmP-rNvfmQ464MH4bGu1ygcg'
INSTA_LINK = 'https://www.instagram.com/p/Caku6ftocfI/?igshid=YmMyMTA2M2Y='
FILE_DIRECTORY = '/home/irina/PycharmProjects/TeleBotforBeauty'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    customer_markup = types.ReplyKeyboardMarkup(True)
    customer_markup.row('Записатися/відмінити')
    customer_markup.row('Послуги та ціни', 'Адреса та контакти')
    customer_markup.row('Підібрати образ', 'Instagram')
    bot.send_message(message.from_user.id, 'Hello', reply_markup=customer_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Записатися/відмінити':
        pass
    elif message.text == 'Послуги та ціни':
        price = 'Price1 = 200uah \n' \
                'price2 = 150uah'
        bot.send_message(message.from_user.id, text=price, parse_mode='html')
    elif message.text == 'Адреса та контакти':
        bot.send_message(message.from_user.id, text='Ландшафтний парк, 1. Вхід з двору.', parse_mode='html')
        bot.send_location(message.from_user.id, 50.42645652952699, 30.562934080980124)
    elif message.text == 'Підібрати образ':
        all_files_in_dir = os.listdir(FILE_DIRECTORY + '/photo')
        random_file = random.choice(all_files_in_dir)
        random_img = open(FILE_DIRECTORY + '/photo/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, random_img)
        random_img.close()
    elif message.text == 'Instagram':
        bot.send_message(message.from_user.id, text=f"<b>{INSTA_LINK}</b>", parse_mode='html')
    # elif message.text == 'stiker':
    #     bot.send_message(message.from_user.id, )


bot.polling(none_stop=True)
