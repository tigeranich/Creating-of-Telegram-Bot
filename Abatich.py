#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyTelegramBotAPI')


# In[2]:


import telebot
from telebot import types
bot = telebot.TeleBot('1816024686:AAEby5EymmmqXm289b7TC9vYmROqiskUaro')


# In[3]:


idk = types.InlineKeyboardMarkup()
answer_yes = types.InlineKeyboardButton(text='А что тогда делать?', callback_data='yes')
idk.add(answer_yes)
answer_no= types.InlineKeyboardButton(text='Ну и ладно', callback_data='no')
idk.add(answer_no)


# In[4]:


how_are_you = types.InlineKeyboardMarkup();
answer_yes1 = types.InlineKeyboardButton(text='Отлично, спасибо!=)', callback_data='good'); 
how_are_you.add(answer_yes1); 
answer_no1 = types.InlineKeyboardButton(text='Бывало и лучше ;)', callback_data='bad');
how_are_you.add(answer_no1)


# In[5]:


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message,f'Меня зовут Абатова-бот. Приятно познакомиться,{message.from_user.first_name}')


# In[6]:


@bot.message_handler(content_types=['text'])
def answer_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == 'салем':
        bot.send_message(message.from_user.id, 'Салеметзизбе!')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо! А у тебя?', reply_markup=how_are_you)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, я Абатова Гульнур, а не Алиса из Яндекса((', reply_markup=idk)


# In[7]:


@bot.callback_query_handler(func=lambda call: True)
def callback_messages(call):
    if call.data == "good":
        bot.send_message(call.message.chat.id, 'Рада за тебя!!! =)')
    elif call.data == "bad":
        bot.send_message(call.message.chat.id, 'Да ничего страшного, я вообще тестовый телеграмм-бот, и не парюсь!=D')
    elif call.data == "yes": 
        bot.send_message(call.message.chat.id, 'Ты можешь написать: "Привет", "Салем", "Как дела?"')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Пока!=)')


# In[ ]:


bot.polling(none_stop=True)


# In[ ]:




