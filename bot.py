import telebot

TOKEN = "7327734495:AAG9dN0Rb4GtODysq1kRPuofeyDADPieI2I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 
        "👋 Сәлем, {0.first_name}!

"
        "📚 "Әлемдік YouTube курсына" қош келдіңіз!

"
        "🔻 Таңдаңыз:
"
        "1️⃣ "Стандарт пакет"
"
        "2️⃣ "Алтын пакет"".format(message.from_user)
    )

@bot.message_handler(func=lambda message: message.text == "1" or "Стандарт" in message.text)
def standard_package(message):
    bot.send_message(message.chat.id, 
        "🎓 "Стандарт пакет"
"
        "💸 Бағасы: "20 000₸" ➝ 50% жеңілдікпен "10 000₸"

"
        "✅ Арна ашу, номер алу, видео монтаж, ниша таңдау, әлемге шығу үйретіледі
"
        "⛔ Кері байланыс жоқ

"
        "💳 Төлем үшін Kaspi👇
"
        "https://pay.kaspi.kz/pay/52bubdrg
"
        "Каспи пэй сілтеме 🔗"
    )

@bot.message_handler(func=lambda message: message.text == "2" or "Алтын" in message.text)
def premium_package(message):
    bot.send_message(message.chat.id, 
        "👑 "Алтын пакет"
"
        "💸 Бағасы: "100 000₸" ➝ 50% жеңілдікпен "50 000₸"

"
        "✅ Барлығы кіреді
"
        "🧑‍💻 1 ай бойы кері байланыс
"
        "🎁 Жеке бренд курсы сыйлыққа!

"
        "💳 Төлем үшін Kaspi👇
"
        "https://pay.kaspi.kz/pay/52bubdrg
"
        "Каспи пэй сілтеме 🔗"
    )

@bot.message_handler(content_types=["photo", "document"])
def handle_receipt(message):
    user_link = "https://t.me/aveadikus1"
    bot.send_message(message.chat.id, 
        "✅ Чек қабылданды!
"
        f"📩 Менеджерге хабарласу: {user_link}"
    )

bot.polling()
