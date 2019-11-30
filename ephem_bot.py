"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


"""
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}
"""

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def planet_constellation(planet):
    if planet == 'Mercury':
        return ephem.constellation(ephem.Mercury(datetime.today()))
    elif planet ==  'Venus':
        return ephem.constellation(ephem.Venus(datetime.today()))
    elif planet ==  'Earth':
        return ephem.constellation(ephem.Earth(datetime.today()))
    elif planet ==  'Mars':
        return ephem.constellation(ephem.Mars(datetime.today()))
    elif planet ==  'Jupiter':
        return ephem.constellation(ephem.Jupiter(datetime.today()))
    elif planet ==  'Saturn':
        return ephem.constellation(ephem.Saturn(datetime.today()))
    elif planet ==  'Uranus':
        return ephem.constellation(ephem.Uranus(datetime.today()))
    elif planet ==  'Neptune':
        return ephem.constellation(ephem.Neptune(datetime.today()))
    elif planet ==  'Pluto':
        return ephem.constellation(ephem.Pluto(datetime.today()))
    else:
        return 'Incorrect planet name, try again please'


def planet_location(bot, update):
    planet = update.message.text.split()[-1].capitalize()
    print(planet)
    result = planet_constellation(planet)
    print(result)
    update.message.reply_text(result)


def main():
    mybot = Updater("1044911545:AAFyjwA7mQFcVl5nGIcrYzxNTiWideWd1wM")
    #, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_location))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()