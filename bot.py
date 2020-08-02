import telebot
import random
from variables import *
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start'])
def send_handler(message):
 chat_id = message.chat.id
 markup = types.ReplyKeyboardMarkup(row_width=1)
 item1 = types.KeyboardButton('Трансформатор силовой')
 markup.add(item1)
 bot.send_message( message.chat.id, "Выберете ЕО", reply_markup= markup )

@bot.message_handler(content_types=['text'])
def send_text(message):
 chat_id = message.chat.id
 markup = types.ReplyKeyboardMarkup(row_width=3)
 item2 = types.KeyboardButton('Система охлаждения')
 item3 = types.KeyboardButton('Бак трансформатора')
 item4 = types.KeyboardButton('Регулятор напряжения без нагрузки (ПБВ)')
 item5 = types.KeyboardButton('ШАОТ')
 item6 = types.KeyboardButton('Маслоохладитель')
 item7 = types.KeyboardButton('Вентилятор')
 item8 = types.KeyboardButton('Насос')
 item9 = types.KeyboardButton('Трубопроводы')
 item10 = types.KeyboardButton('Арматура запорная')
 item11 = types.KeyboardButton('Фильтр')
 item12 = types.KeyboardButton('Контрольно-измерительная аппарутура')
 item13 = types.KeyboardButton('Расширительный бак')
 item14 = types.KeyboardButton('Нижняя часть бака')
 item15 = types.KeyboardButton('Верхняя часть бака ("колокол")')
 item16 = types.KeyboardButton('Элементы крепления')
 item17 = types.KeyboardButton('Избиратель')
 item19 = types.KeyboardButton('Сбои в работе ШАОТ')
 item20 = types.KeyboardButton('Загрязнение поверхности')
 item21 = types.KeyboardButton('Течь масла')
 item22 = types.KeyboardButton('Разрушение уплотнений')
 item23 = types.KeyboardButton('Повышенный шум')
 item24 = types.KeyboardButton('Механические повреждения')
 item25 = types.KeyboardButton('Привод')
 item26 = types.KeyboardButton('Привод')
 item27 = types.KeyboardButton('Привод')
 item28 = types.KeyboardButton('Привод')

 if message.text == 'Трансформатор силовой':
  markup.add(item2, item3, item4)
  bot.send_message(message.chat.id, "Выберете конструктивный элемент", reply_markup=markup)
 elif message.text == 'Система охлаждения':
  markup.add(item5, item6, item7, item8, item9, item10, item11, item12)
  bot.send_message(message.chat.id, "Выберете типовой узел", reply_markup=markup)
 elif message.text == 'Бак трансформатора':
  markup.add(item13, item14, item15, item16)
  bot.send_message(message.chat.id, "Выберете типовой узел", reply_markup=markup)
 elif message.text == 'Регулятор напряжения без нагрузки (ПБВ)':
  markup.add(item16, item17, item18)
  bot.send_message(message.chat.id, "Выберете типовой узел", reply_markup=markup)

bot.polling(none_stop=True, interval=0)