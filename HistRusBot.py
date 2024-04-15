import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import emoji


API_TOKEN = 'Token'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['hello'])
def greeting(message):
    bot.send_message(message.chat.id, f'\nПриветствую! Я бот-помощник по Истории России'
                                      '\n'
                                      '\nЯ храню в себе всю историю с древних, не запамятных времен по настоящее время.'
                                      '\nНу и много других вещей'
                                      '\nДля старта напиши команду /start.'
                                      '\n'
                                      '\n'
                                      'Developed by shtemisu', 'html')


@bot.message_handler(commands=['help'])
def helping(message):
    bot.send_message(message.chat.id, '<em><b>Help information</b></em>'''
                                      '\n'
                                      '\nЕсли у вас возникли проблемы, прошу обращайтесь'
                                      '\nК.т:  <b>8914-228-63-29</b>'
                                      '\nГл.разработчик: Роман', 'html')


@bot.message_handler(commands=['aboutUs'])
def dev(message):
    bot.send_message(message.chat.id, '<b>Создано специально для дисциплины "История России"</b>'
                                      '\n'
                                      '<b>\nРазработали студенты СВФУ им М.К. Аммосова</b>'
                                      '<b>\nИнститута математики и информатики,группы ИТСС-23:</b>'
                                      '\n'
                                      '\nПинигин Роман'
                                      '\nЕфимов Тимофей'
                                      '\nАммосов Александр'
                                      '\nСыроватский Айысхан'
                                      '\nКолодезников Еремей', 'html')


@bot.message_handler(commands=['start'])
def menu(a):
    mainmenu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Привет!' + emoji.emojize(':waving_hand:'),
                                      callback_data='key1')
    key2 = types.InlineKeyboardButton(text='О нас' + emoji.emojize(':alien_monster:'),
                                      callback_data='key2')
    key3 = types.InlineKeyboardButton(text='Помощь' + emoji.emojize(':crossed_fingers:'),
                                      callback_data='key 3')
    key4 = types.InlineKeyboardButton(text='Начать поиск...' + emoji.emojize(':magnifying_glass_tilted_left:'),
                                      callback_data='key4')
    key5 = types.InlineKeyboardButton(text='Поддержать нас' + emoji.emojize(':money_with_wings:'),
                                      callback_data = 'key4')

    mainmenu.add(key1, key2, key3, key4, key5)
    bot.send_message(a.chat.id, 'Тыкни кнопочку:)', reply_markup=mainmenu)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Привет!'+emoji.emojize(':waving_hand:'),
                                          callback_data='key1')
        key2 = types.InlineKeyboardButton(text='О нас'+emoji.emojize(':alien_monster:'),
                                          callback_data='key2')
        key3 = types.InlineKeyboardButton(text='Помощь'+emoji.emojize(':crossed_fingers:'),
                                          callback_data='key 3')
        key4 = types.InlineKeyboardButton(text='Начать поиск...'+emoji.emojize(':magnifying_glass_tilted_left:'),
                                          callback_data='key4')
        #key5 = types.InlineKeyboardButton(text='Поддержать нас' + emoji.emojize(':money_with_wings:'),
                                         # callback_data='key4')
        mainmenu.add(key1, key2, key3, key4)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "key1":
        next_menu = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu.add(back)
        bot.edit_message_text('\nПриветствую! Я бот-помощник по Истории России'
                              '\n'
                              '\nЯ храню в себе всю историю с древних, не запамятных времен по настоящее время.'
                              , call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu, parse_mode='html')
    elif call.data == "key2":
        next_menu2 = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu2.add(back)
        bot.edit_message_text('<b>Создано специально для дисциплины "История России"</b>'
                              '\n'
                              '<b>\nРазработали студенты СВФУ им М.К. Аммосова</b>'
                              '<b>\nИнститута математики и информатики,группы ИТСС-23:</b>'
                              '\n'
                              '\nПинигин Роман'
                              '\nЕфимов Тимофей'
                              '\nАммосов Александр'
                              '\nСыроватский Айысхан'
                              '\nКолодезников Еремей', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2, parse_mode='html')
    elif call.data == "key3":
        next_menu3 = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu3.add(back)
        bot.edit_message_text('<em><b>Help information</b></em>'''
                              '\n'
                              '\nЕсли у вас возникли проблемы, прошу обращайтесь'
                              '\nК.т:  <b>8914-228-63-29</b>'
                              '\nГл.разработчик: Роман', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu3, parse_mode='html')
    elif call.data == 'key4':
        next_menu3 = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu3.add(back)
        bot.send_message(call.message.chat.id, +emoji.emojize(':thinking_face:')+'Введите запрос...')

        @bot.message_handler(func=lambda call: True)
        def callback_wiki(message):
            text = message.text
            url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + text
            request = requests.get(url)
            s = BeautifulSoup(request.text, "html.parser")
            links = s.find_all("div", class_="mw-search-result-heading")
            if len(links) > 0:
                url = "https://ru.wikipedia.org" + links[0].find("a")["href"]
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            driver = webdriver.Chrome(option)
            driver.get(url)

            driver.execute_script("window.scrollTo(200,200)")
            driver.save_screenshot("img.png")
            driver.close()
            photo = open("img.png", "rb")
            bot.send_photo(message.chat.id, photo, 'Ссылка на статью:'+url, parse_mode='html')


bot.polling(non_stop=True)
