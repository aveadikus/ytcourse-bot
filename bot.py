# -*- coding: utf-8 -*-
import telebot

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "📢 Қош келдіңіз!

"
        "🎓 Бұл жерде сіз YouTube курсына жазыла аласыз.
"
        "Төмендегі пакеттердің бірін таңдаңыз:

"
        "💼 *Стандарт пакет* – 15 000 ₸ (50% жеңілдікпен)
"
        "🪙 *Алтын пакет* – 75 000 ₸ (1 ай кері байланыс)

"
        "💳 Төлем үшін карта: 4400 1234 5678 9012
"
        "🧾 Төлем жасаған соң, чекті маған жеке жіберіңіз: @aveadikus"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, "Сізге көмектесу үшін осындамын. Төлем жасаған соң, чек жіберіңіз. 📩")

bot.infinity_polling()
