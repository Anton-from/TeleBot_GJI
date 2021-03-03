#print ('Здарова! я, бля, всетаки работаю!!!')

import telebot
import requests
import openpyxl
import pandas as pd


# Тупо скачиваем и открываем файл в ручную 
link = 'https://www.gosgil42.ru/upload/litsenzirovanie/%D0%9A%D0%BE%D0%BF%D0%B8%D1%8F%20ree_spis_dom01032021.xlsx'
r = requests.get(link, allow_redirects=True)
file = 'dataBaseYK.xlsx'
#open(filename, 'wb').write(r.content)


#Парсим сайт гжи и качаем файл реестра всех управляшек


#Парсим скаченный excel файл  и ищим совпадения
excel_data_df = pd.read_excel(file, sheet_name='Лист1', header=3)

print(excel_data_df.columns.ravel())



#book = openpyxl.open(file,read_only=True)
#sheet = book.active

#for row in range(6,16):
#    city = sheet[row][2].value
#    street = sheet[row][3].value
#    numer_home = sheet[row][4].value
#    service_home = sheet[row][13].value
#    print(row, city, street, numer_home, service_home)


#Сохраняем полученные данные в строку и передаем в телеграмм бот




#Блок работы бота
TOKEN = '1654985626:AAERGW-HUshvULF_P66TQf0MeMnzuB3FpCw'
bot = telebot.TeleBot(TOKEN)

#Прикручиваем поиск
@bot.message_handler(commands=['search_videos'])
def search_videos(message):
    msg = bot.send_message(message.chat.id, "Какой город тебя интересует?")
    bot.register_next_step_handler(msg, search)


#Текст
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет!')

    elif message.text.lower() == "дай ссылку":
        bot.send_message(message.chat.id, 'https://www.gosgil42.ru/upload/litsenzirovanie/%D0%9A%D0%BE%D0%BF%D0%B8%D1%8F%20ree_spis_dom01032021.xlsx')
    elif message.text.lower() == "помоги":
        msg = bot.send_message(message.chat.id, "Какой город тебя интересует?")
        bot.register_next_step_handler(msg, search)
        #bot.register_next_step_handler(search_videos)
    else:
        bot.send_message(message.chat.id, 'Извини, я пока что могу только поздороваться если ты мне напишешь "Привет" или кинуть сслыку на реестр управляшек если напишешь "Дай ссылку". Так же помошь попробовать написать мне "помоги" и я попробую найти какая управляшка в интересующем доме, но не найду, алгоритм пока до конца не прогружен')
#Поиск
def search(message):
    bot.send_message(message.chat.id, 'Попробую что нибудь найти')

    
    
    
bot.polling()