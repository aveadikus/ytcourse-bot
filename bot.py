import telebot

TOKEN = "7327734495:AAG9dN0Rb4GtODysq1kRPuofeyDADPieI2I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = f"👋 Сәлем, {message.from_user.first_name}!"           
    
    "📚 *Әлемдік YouTube курсы* туралы ақпарат:"     
    
    "💼 *Стандарт пакет* — ~20 000₸~ → *10 000₸*"      
    
    "✅ Арна ашу"
"✅ Номер алу"
"✅ Видео монтаждау"          
"✅ Ниша таңдау"
"✅ Әлемге шығу"
"(Кері байланыс жоқ)"

           "👑 *Алтын пакет* — ~100 000₸~ → *50 000₸*"
            "✅ Барлығы кіреді"
"✅ 1 ай кері байланыс"
"🎁 Жеке бренд курсы сыйлыққа"

"💳 *Төлем сілтемесі (Kaspi Pay)*:
👉 https://pay.kaspi.kz/pay/52bubdrg"

    "Төлем жасаған соң, чекті маған жіберу үшін осы сілтемеге өтіңіз:"     
       "👉 https://t.me/aveadikus1"
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

bot.polling()
