import telebot
from telebot import types
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Token қоршаған ортадан алынады
OWNER_ID = os.environ.get("OWNER_ID")  # Иесі (сатушы) ID

bot = telebot.TeleBot(TOKEN)

# Бастапқы хабарлама
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("💼 Стандарт пакет", callback_data='standard'),
        types.InlineKeyboardButton("👑 Алтын пакет", callback_data='gold')
    )
    bot.send_message(message.chat.id, "Курс таңдаңыз:", reply_markup=markup)

# Түйме басылғанда
@bot.callback_query_handler(func=lambda call: True)
def handle_package_selection(call):
    if call.data == 'standard':
        text = "💼 *Стандарт пакет*"
💸 Бағасы: *20 000₸* → 50% жеңілдікпен *10 000₸*

Төлем реквизиті:
"https://pay.kaspi.kz/pay/52bubdrg\n\n"

🧾 Чек жіберген соң, сізге курс жіберіледі."
    elif call.data == 'gold':
        text = "👑 *Алтын пакет*"
💸 Бағасы: *150 000₸* → 50% жеңілдікпен *75 000₸*
📩 1 ай кері байланыс

Төлем реквизиті:
"https://pay.kaspi.kz/pay/52bubdrg\n\n"

🧾 Чек жіберген соң, сізге курс жіберіледі."
    else:
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🧾 Чекті жіберу")
    bot.send_message(call.message.chat.id, text, reply_markup=markup, parse_mode='Markdown')

# Чек жібергенде
@bot.message_handler(func=lambda message: "чек" in message.text.lower())
def handle_receipt(message):
    user_info = f"👤 @{message.from_user.username} | {message.from_user.id}"
    if message.photo:
        bot.send_message(message.chat.id, "✅ Чек қабылданды! Курсты күтіңіз.")
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"📩 Маған жазу үшін: [Тікелей байланыс](https://t.me/{bot.get_me().username})", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "📸 Чек фотосын жіберіңіз!")

bot.infinity_polling()
