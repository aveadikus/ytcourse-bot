import telebot

TOKEN = "7327734495:AAG9dN0Rb4GtODysq1kRPuofeyDADPieI2I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    text = (
        f"Сәлем, {first_name}! 👋\n\n"
        "📚 *Әлемдік YouTube курсы туралы толық ақпарат:*\n\n"
        "🎓 *Стандарт пакет* — ~20 000₸~ → *10 000₸*\n"
        "🔹 Арна ашу, номер алу, видео монтаж, ниша таңдау, әлемге шығу жолдары.\n"
        "❌ Кері байланыс қарастырылмаған.\n\n"
        "💎 *Алтын пакет* — ~100 000₸~ → *50 000₸*\n"
        "✅ Барлығы + 1 ай бойы кері байланыс\n"
        "🎁 Жеке бренд курсы сыйлыққа беріледі.\n\n"
        "💳 *Төлем жасау үшін Kaspi:*\n"
        "https://pay.kaspi.kz/pay/52bubdrg\n"
        "📌 Kaspi Pay сілтеме 👆\n\n"
        "✅ Төлем жасаған соң, чекпен бірге маған жекеге жазыңыз: @aveadikus1"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

bot.polling()
